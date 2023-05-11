# file-run2
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/267/)

## Description
> Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?

## What It Does
Binary print out different information according to the argument.
```bash
$ ./run 
Run this file with only one argument.

$ ./run A
Won't you say 'Hello!' to me first?
```

## Solution
Run the provided binary, `run`, with argument mentioned in the description as:
```bash
./run Hello!
```
and get the **flag**.