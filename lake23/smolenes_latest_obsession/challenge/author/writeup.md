<style>
body {
  margin: auto;
  max-width: 50em;
}
</style>

# writeup for smolene's latest obsession

This is the writeup of a challenge from LakeCTF qualifications 2023.

Writeup and challenge by @smolene.

I will try to explain the vm and the chal. It is not necessary at all to understand everything to solve the chal, but hopefully you can find the vm as interesting as I do :)

## 1. Summary

The global plan of attack is as such: 

- reverse the binary and understand that it implements an interpreter.
- read the chal description to understand that the remote has more input given to it before you
- write some code for the interpreter to leak the rest of the input only present on the remote (the "prompt").
- reverse the "prompt", notice that it implements a flag checker.
- solve the flagchecker.
- ???
- profit

The server runs (basically) this:
```
ncat -lk 8080 -c 'bash runchal.bash'
# runchal.bash is just this:
# cat prompt - | ./chal
```

## 2. Introduction to Forth and indirect threaded code

The binary is some hand written x86 assembly (source in f.nasm) implementing a very simple Forth. 
The control flow may seem complex but it is built out of very simple parts:

- general stuff:
  - 1 cell = 4 bytes
  - stack counted in units of cells
  - esp points to the data stack
  - ebp points to the return stack
  - it is a stack machine, operands are fetched from the stack and results written to it
- indirect threaded code:
  - slightly unintuitive way of storing code, see next paragraphs
- at the start of a primitive (nest_, unnest_, read_, etc):
  - esi points to the next instruction in the parent word
  - eax points to the start of the current block

format of a header/block:
index in cells (1 cell = 4 bytes)
```
0 pointer to next header
1 name of word
2 continued..
3 continued.. (12B total, 0 padded)
4 flags (0b1 = immediate, others unused)
- - - - header ^^^
- - - - block  vvv
5 pointer to interpreter of current block
6 data ...
7 data ... etc
8 ...
```

Every forth function (called a word) is stored as a block. Blocks are linked together in a linked list. 
Looking up a function is just walking the list until you arrive at a header with the name you are looking for.

Every block has its own interpreter (cell 5), which is a pointer to native code, which will do things with the data following it.
An interpreter may need no data, like most binary-operation words (like add, sub etc).
Almost every interpreter will follow a convention that allows it to execute code by simply concatenating addresses of blocks.
The macro `next` will take `esi` (= address of next block) and deref it and put the result in `eax`, then increment `esi` ; then, it jumps to `[eax]`.

```
block1:
&interp
ptr = &block2
ptr = &block3   <-- esi points here at the start of executing [block2]
ptr = etc..     <-- esi points here at the end (incremented by esi)


block2:
&interp          <-- eax points here at the start of executing [block2]
ptr
ptr

block3:
&interp
ptr
ptr
```

In assembly:
```
my_interp:
;; esi is next pointer in caller block, eax is pointer to start of callee block
... whatever assembly you want ...
lodsd     ;; get next pointer in caller block
jmp [eax] ;; jump interp of next block
;; abbreviated as `next` in f.nasm
```

From here, we can write a special routine `nest_`, which is an interpreter that will allow writing words (functions).
Indeed, `nest` pushes the value of `esi` on the return stack (so the return address), then sets the address of the "next block to execute" (=`esi`) to `eax+4`, which is the data that follows the `nest_`.
To complement it, `unnest_` pops the return address from the return stack and sets the "next block to execute" (=`esi`) to it.
We now have function calls:

```
main:
&nest_ <-- interp
&foo   <-- interp sees the rest of the block as the "body of the function"
&bar
&baz
&unnest

foo:
&nest_ <-- interp
&bla
&blu
&blo
&unnest

etc..
```

Not every block starts with `nest_`: instead, all basic operations are implemented in assembly with an "interpreter" that performs it.
For instance, addition is implemented as such:

```
add_:
... assembly code ... (see in f.nasm)
next

unnest_:
... assembly code ...
next

add:
&add_ <-- interp (not nest_!!)
      <-- no need for extra data

unnest:
&unnest_

main:
&nest_
&add  <-- points to block, not function
...
&unnest <-- note that unnest is also a pointer to a block, not to assembly

```

Hopefully you start to understand the structure. The implementation of `push_` may also be interesting for you to understand.
It takes the next value in the caller block and pushes it on the stack, so you can have constants within the code.
```
push:
&push_

foo:
&nest
&push
123
&push
456
&add
&unnest
```

foo pushes 123, then 456, then sums them up together.

## 3. Bootstrapping the repl

We can now write code in this weird little language by concatenating addresses in memory. This is exactly what is happening in the .data section.
I made a few macros to define words (`mkw` etc) with which i made a REPL called `outer` here (for outer interpreter, by opposition to the inner interpreters).

This interpreter is simple:
```
loop:
  read word from stdin (whitespace separated, max 12 chars because of static buffers lmao)
  if outermode == 0: // > in call mode
    lookup word in dictionary (the linked list of blocks)
    call it
  else: // > in compile mode
    if word is number:
      append push to block currently compiled
      append <word as number> ...
    else:
      lookup word in dict
      if flag 0b1 is set: // > word is immediate, so call it even in compile mode
        call word
      else:
        append pointer to block (cell 5 in diagram above)
```

Thus writing words will run them, until some word writes the `outermode` variable to 1, after which every word is appended instead.
`:` sets up a new header with the name of the block taken as the next word from stdin, then sets `outermode` to 1.
`;` finishes a word and puts `outermode` back to 0.

One can define a function like this `: addone 1 + ;`, or a function to print the top item of the stack `: . tostr puts 10 putc ;`.
Try it!
```
$ ./chal
: addone 1 + ;
: . tostr puts 10 putc ;
3 addone addone .
```
(should print back "5")

Notice that some words dont have the same name in the interpreter: the macro `mkws` lets me rename the word (for `add` it is renamed to `+` for instance).

## 4. Writing forth

And now the prompt! This file is given as input to the chal binary on the server, so the remote has extra words that you don't have locally.
You need to leak these words.
An easy way is to notice that the binary is always mapped to the same address, thus you can simply dump the binary data from the start of the .bss section.
With a few experiments you can see that new words are all written in the .bss (as well as the stack and return stack, although that doesnt matter here), and thus the words from the prompt will be written there in memory on the remote.

```
$ gdb ./chal
run
<Ctrl-C>
# check where data section starts
vmmap
[ Legend:  Code | Heap | Stack ]
Start      End        Offset     Perm Path
0x8048000 0x804a000 0x000000 r-x ./chal
0x804a000 0x804b000 0x002000 rwx ./chal
0x804b000 0x805b000 0x000000 rwx [heap]
0xf7ff8000 0xf7ffc000 0x000000 r-- [vvar]
0xf7ffc000 0xf7ffe000 0x000000 r-x [vdso]
0xfffdd000 0xffffe000 0x000000 rwx [stack]

# .bss is 0x804b000
```

Then write a little forth word that you can give to the remote to leak all of that.
```
ncat -l 8080 -c 'bash runchal.bash' &
ncat localhost 8080 | tee log
: . tostr puts 10 putc ;
: pbyte @ . ;
: leakall dup pbyte 1 + tail leakall ;
134524928 leakall
```
134524928 is decimal for 0x804b000.
tail is a word that tail-calls the next word, to avoid overflowing the stack with a loop.
I mean you can also just make a loop in python like so (untested):
```
for i in range(0x10000//4):
  print(f'{i} @ tostr puts 10 putc')
```

Now you have all the data from the remote! From that, you can reconstruct functions and datastructures from the prompt, as well as the flagchecker.

Maybe looking at the prompt in text form can make it easier to understand.
Also maybe not. I was very late when making this chal and the prompt is really ugly and bad haha.

Another way of leaking the prompt is to simply write shellcode in the .data section and jump to it, since it is executable because of a quirk in how the linker behaves with small section sizes and alignment. Then `cat prompt` :3
That's left as an exercise for the reader.

## 5. Reversing the prompt

By looking at the strings of the prompt, you can see that a word is called `flagchecker`.
Calling `flagchecker EPFL{myflag}` will tell you if the flag is correct or not.
The flagchecker is a simple substitution table, it iterates over every character, looksup the coded char in the substitution table `b`.
Then it checks in the already substitued string `cf` if the substituded char matches. If it does, then the character was correct!
The checker unsets the `hihi` flag if a char is wrong, and its value is tested at the end to check if it was the correct flag.

To find the flag, simply invert the `b` substitution table and run `cf` through it, and you're done!

# Conclusion

It was a very fun chal to make, I hope it was also fun to play.
I have made numerous improvements to the forth in the meantime, so many things are better now. Maybe one day I'll publish a more polished version of it :)

I also didn't explain everything here, I hope you can understand the missing pieces by looking at the source.

Thanks for reading!

