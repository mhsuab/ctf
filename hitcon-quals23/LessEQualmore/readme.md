# LessEQualmore

## Description
> HITCON CTF 2023 Quals
> 
> LessEQualmore [248pts]  
> Sometime, less ~~instruction~~ equal more ~~instruction~~ ...
> 
> Author: bronson113
> 33 Teams solved.

Also, provide a [binary file](./LessEQualmore) and a [text file](./chal.txt) with `nc chal-lessequalmore.chal.hitconctf.com 11111`.

However, for this challenge, we do not need the remote connection.

```bash
> ./lessequalmore chal.txt
*** Flag Checker ***
asdfasdfasdf
You entered:
asdfasdfasdf
Sorry, wrong flag!
```

## Analysis
The [binary](./lessequalmore) simply reads `chal.txt` and start interpreting the instructions.  
([chal.txt](./chal.txt) contains all the instructions needed to check the flag)

possible instructions based on the instruction:  
(for instruction [a1, a2, a3])
| order |   condition    | `True`        | `False`            | description      |
| :---: | :------------: | ------------- | ------------------ | ---------------- |
|   1   |    `a1 < 0`    | from input    | `mem[a1]`          | return `value`   |
|   2   |    `a2 < 0`    | print `value` | `mem[a2] -= value` |                  |
|   3   | `mem[a2] <= 0` | goto a3       | next instruction   | conditional jump |

Therefore, the binary is a simple VM that reads instructions from `chal.txt` and execute them. To get more infomation from the execution, re-implement the VM in python.

## Python Interpreter/Debugger/Trace
> python interpreter [here](./interp.py)

> `get_bignum` contains more logic than what is use in the challenge. My guess is that those are for the next challenge, `SUBformore`. Therefore, this function will just treat it as **getting input and return its negation**.

Besides interpreting the instructions, the python interpreter also provides other functionalities:
|       command        | functionality                                        | additional description                                         |
| :------------------: | :--------------------------------------------------- | :------------------------------------------------------------- |
|       `reset`        | reset the VM                                         | reset the VM to initial state                                  |
|  `trace <filename>`  | trace the execution                                  | trace the execution and save the result to `<filename>`        |
|     `c(ontinue)`     | continue the execution                               |                                                                |
|    `r(un) <flag>`    | run the execution                                    | run the execution from the beginning with the specify `<flag>` |
|       `s(tep)`       | step into the next instruction                       |                                                                |
|       `i(nfo)`       | print the current state                              |                                                                |
|      `b <line>`      | set breakpoint at `<line>`                           |                                                                |
|      `u <line>`      | unset breakpoint at `<line>`                         |                                                                |
|       `q(uit)`       | quit the interpreter                                 |                                                                |
| `e <python command>` | evaluate `<python command>`                          |                                                                |
|       `input`        | print out buffer from 16-th, with 8 chunks of size 8 | print out buffer where the input is                            |
|       `target`       | print out buffer from 98-th with 8 chunks of size 8  | print out buffer where the target of the comparison is         |

### Side Channel: Instruction Count
Since we know that the flag start with `hitcon{`, we can use the instruction count to try to brute force the flag.
> brute force the next character with [script](./brute.py)

Result:
```bash
> python3 brute.py
...
q: 134932
r: 135869
s: 134933
t: 134933
u: 134933
v: 134933
w: 134931
x: 134936
y: 134936
...
max_char: r
max_count: 135869
second_max_count: 134945
diff: 924
...
```

Input, `hitcon{r`, has significantly more instructions than other inputs. Therefore, we can conclude that the next character is `r`.

However, when we try to brute force the next character, we got the following result:
```bash
> python3 brute.py
...
max_char: b'\t'
max_count: 136603
second_max_count: 136602
diff: 1
```

That is, the number of instructions are almost the same. Therefore, the instruction count cannot be used to brute force the entire flag.

### Instruction Trace
> Try to find out the instruction corresponding to the increase of the instruction count for `hitcon{r`.
Thanks to @babaisflag for adding the trace in the file.

[hitcon_r](./hitcon_r.trace) and [hitcon_s](./hitcon_s.trace) are the trace for `hitcon{r` and `hitcon{s` respectively and from line 133535 in [hitcon_r](./hitcon_r.trace#L133535), the trace has a big chunk of additional instructions. This should be the instruction for additional comparison after the program verify the first 8 characters.

The main difference from the trace is that the instruction @ `pc = 3320` jump to `pc = 3386` instead of `pc = 3323` for `hitcon{r` and `pc = 3320` occurs 9 times for `hitcon{r` and 1 times for `hitcon{s`. Therefore, this instruction to be the one that compare something that depends on the input with the target value which `hitcon{r` passes the first 8 checks but fails the 9th check. Also, even though two inputs have the same prefix, `hitcon{s` did not pass any of the checks; thus, guess that the program will do some computation on the input first and then compare for every 8 characters which is the reason why the method of [brute force](#side-channel-instruction-count) will not work for the 9-th character, and brute force 8 characters at a time is not feasible.

Therefore, the instruction from [line_133444](./hitcon_r.trace#L133444) to [line_133511](./hitcon_r.trace#L133511), part for first check, is the one that we need to focus on.

<details>
<summary>Partial Instruction Trace</summary>

```asm
@  3110: mem[0] -= mem[0] (0); (0 -= 0)jmp 3114
@  3114: mem[4] -= mem[4] (56); (56 -= 56)jmp 3117
@  3117: mem[0] -= mem[3113] (0); (0 -= 0)jmp 3120
@  3120: mem[4] -= mem[0] (0); (0 -= 0)jmp 3123
@  3123: mem[0] -= mem[0] (0); (0 -= 0)jmp 3126
@  3126: mem[0] -= mem[6] (0); (0 -= 0)jmp 3129
@  3129: mem[4] -= mem[0] (0); (0 -= 0)jmp 3132
@  3132: mem[0] -= mem[0] (0); (0 -= 0)jmp 3135
@  3135: mem[4] -= mem[15] (-16777216); (0 -= -16777216)
@  3138: mem[4] -= mem[14] (16777216); (16777216 -= 16777216)jmp 3141
@  3141: mem[4] -= mem[0] (0); (0 -= 0)jmp 3147
@  3147: mem[0] -= mem[4] (0); (0 -= 0)jmp 3156
@  3156: mem[0] -= mem[0] (0); (0 -= 0)jmp 3159
@  3159: mem[0] -= mem[4] (0); (0 -= 0)jmp 3162
@  3162: mem[1] -= mem[0] (0); (0 -= 0)jmp 3165
@  3165: mem[0] -= mem[0] (0); (0 -= 0)jmp 3168
@  3168: mem[0] -= mem[12] (16); (0 -= 16)jmp 3171
@  3171: mem[1] -= mem[0] (-16); (0 -= -16)
@  3174: mem[0] -= mem[0] (-16); (-16 -= -16)jmp 3177
@  3177: mem[4] -= mem[4] (0); (0 -= 0)jmp 3180
@  3180: mem[0] -= mem[1] (16); (0 -= 16)jmp 3183
@  3183: mem[3192] -= mem[3192] (0); (0 -= 0)jmp 3186
@  3186: mem[3192] -= mem[0] (-16); (0 -= -16)
@  3189: mem[0] -= mem[0] (-16); (-16 -= -16)jmp 3192
@  3192: mem[0] -= mem[16] (16774200); (0 -= 16774200)jmp 3195
@  3195: mem[4] -= mem[0] (-16774200); (0 -= -16774200)
@  3198: mem[0] -= mem[0] (-16774200); (-16774200 -= -16774200)jmp 3201
@  3201: mem[1] -= mem[1] (16); (16 -= 16)jmp 3204
@  3204: mem[0] -= mem[0] (0); (0 -= 0)jmp 3208
@  3208: mem[5] -= mem[5] (65); (65 -= 65)jmp 3211
@  3211: mem[0] -= mem[3207] (82); (0 -= 82)jmp 3214
@  3214: mem[5] -= mem[0] (-82); (0 -= -82)
@  3217: mem[0] -= mem[0] (-82); (-82 -= -82)jmp 3220
@  3220: mem[0] -= mem[6] (0); (0 -= 0)jmp 3223
@  3223: mem[5] -= mem[0] (0); (82 -= 0)
@  3226: mem[0] -= mem[0] (0); (0 -= 0)jmp 3229
@  3229: mem[5] -= mem[15] (-16777216); (82 -= -16777216)
@  3232: mem[5] -= mem[14] (16777216); (16777298 -= 16777216)
@  3235: mem[5] -= mem[0] (0); (82 -= 0)
@  3238: mem[0] -= mem[0] (0); (0 -= 0)jmp 3232
@  3232: mem[5] -= mem[14] (16777216); (82 -= 16777216)jmp 3235
@  3235: mem[5] -= mem[0] (0); (-16777134 -= 0)jmp 3241
@  3241: mem[0] -= mem[5] (-16777134); (0 -= -16777134)
@  3244: mem[0] -= mem[0] (16777134); (16777134 -= 16777134)jmp 3247
@  3247: mem[5] -= mem[15] (-16777216); (-16777134 -= -16777216)
@  3250: mem[0] -= mem[0] (0); (0 -= 0)jmp 3253
@  3253: mem[0] -= mem[5] (82); (0 -= 82)jmp 3256
@  3256: mem[1] -= mem[0] (-82); (0 -= -82)
@  3259: mem[0] -= mem[0] (-82); (-82 -= -82)jmp 3262
@  3262: mem[0] -= mem[12] (16); (0 -= 16)jmp 3265
@  3265: mem[1] -= mem[0] (-16); (82 -= -16)
@  3268: mem[0] -= mem[0] (-16); (-16 -= -16)jmp 3271
@  3271: mem[5] -= mem[5] (82); (82 -= 82)jmp 3274
@  3274: mem[0] -= mem[1] (98); (0 -= 98)jmp 3277
@  3277: mem[3286] -= mem[3286] (0); (0 -= 0)jmp 3280
@  3280: mem[3286] -= mem[0] (-98); (0 -= -98)
@  3283: mem[0] -= mem[0] (-98); (-98 -= -98)jmp 3286
@  3286: mem[0] -= mem[98] (16774200); (0 -= 16774200)jmp 3289
@  3289: mem[5] -= mem[0] (-16774200); (0 -= -16774200)
@  3292: mem[0] -= mem[0] (-16774200); (-16774200 -= -16774200)jmp 3295
@  3295: mem[1] -= mem[1] (98); (98 -= 98)jmp 3298
@  3298: mem[0] -= mem[0] (0); (0 -= 0)jmp 3302
@  3302: mem[0] -= mem[4] (16774200); (0 -= 16774200)jmp 3305
@  3305: mem[1] -= mem[0] (-16774200); (0 -= -16774200)
@  3308: mem[0] -= mem[0] (-16774200); (-16774200 -= -16774200)jmp 3311
@  3311: mem[1] -= mem[5] (16774200); (16774200 -= 16774200)jmp 3314
@  3314: mem[1] -= mem[0] (0); (0 -= 0)jmp 3320
@  3320: mem[0] -= mem[1] (0); (0 -= 0)jmp 3386
```
</details>

### Memory: Input and Target Buffer
Figure out the buffers from debugging and the trace.

#### Input Buffer
Program will print out the input all at once during the execution. That is, the input should be stored in some part of the memory. Therefore, break when the program start printing the input and search the memory for the input.

Break at `5325` where the program print and wait until it print `Y`, start of `You entered:`.
```bash
python3 interp.py
> b 5325
> r hitcon{r
breakpoint at 5325
> c
*breakpoint at 5325
...
Ybreakpoint at 5325
> 
obreakpoint at 5325
> e print (''.join(chr(i) if i < 256 and i >= 0 else '\0' for i in self.mem).find(self.flag))
eval: print (''.join(chr(i) if i < 256 and i >= 0 else '\0' for i in self.mem).find(self.flag))
16
> u 5325
> c
> e print (self.mem[16:100])
eval: print (self.mem[16:100])
[16774200, 1411, 16776275, 3646, 1532, 6451, 2510, 16777141, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16774200, 1411]
```

That is, the input is stored from `16`-th memory address and the value at the location will be modified during the execution.

#### Target Buffer
We had figure out where the input is stored. Now, we need to figure out where the target buffer is stored. Dig into the trace and find out where the target buffer is stored.

First Check: value, `16774200`, compare with somewhere in the memory,
```asm
...
@  3177: mem[4] -= mem[4] (0); (0 -= 0)jmp 3180
@  3180: mem[0] -= mem[1] (16); (0 -= 16)jmp 3183
@  3183: mem[3192] -= mem[3192] (0); (0 -= 0)jmp 3186
@  3186: mem[3192] -= mem[0] (-16); (0 -= -16)
@  3189: mem[0] -= mem[0] (-16); (-16 -= -16)jmp 3192
@  3192: mem[0] -= mem[16] (16774200); (0 -= 16774200)jmp 3195
@  3195: mem[4] -= mem[0] (-16774200); (0 -= -16774200)
@  3198: mem[0] -= mem[0] (-16774200); (-16774200 -= -16774200)jmp 3201
@  3201: mem[1] -= mem[1] (16); (16 -= 16)jmp 3204
...
@  3280: mem[3286] -= mem[0] (-98); (0 -= -98)
@  3283: mem[0] -= mem[0] (-98); (-98 -= -98)jmp 3286
@  3286: mem[0] -= mem[98] (16774200); (0 -= 16774200)jmp 3289
@  3289: mem[5] -= mem[0] (-16774200); (0 -= -16774200)
@  3292: mem[0] -= mem[0] (-16774200); (-16774200 -= -16774200)jmp 3295
@  3295: mem[1] -= mem[1] (98); (98 -= 98)jmp 3298
@  3298: mem[0] -= mem[0] (0); (0 -= 0)jmp 3302
@  3302: mem[0] -= mem[4] (16774200); (0 -= 16774200)jmp 3305
@  3305: mem[1] -= mem[0] (-16774200); (0 -= -16774200)
@  3308: mem[0] -= mem[0] (-16774200); (-16774200 -= -16774200)jmp 3311
@  3311: mem[1] -= mem[5] (16774200); (16774200 -= 16774200)jmp 3314
@  3314: mem[1] -= mem[0] (0); (0 -= 0)jmp 3320
@  3320: mem[0] -= mem[1] (0); (0 -= 0)jmp 3386
```

At instruction `3286`, load the value from `mem[98]` to `mem[0]` and then use the loaded value to compare with the computed input. Therefore, the target buffer should be stored at `mem[98]` onwards.

Also, when searching for the buffer that store all the hardcoded output strings, it is starting from `mem[162]`.
That is, the target buffer should be stored from `mem[98]` to `mem[161]`.
```bash
> target
98: [16774200, 1411, 16776275, 3646, 1532, 6451, 2510, 16777141]
106: [16775256, 2061, 16776706, 2260, 2107, 6124, 878, 16776140]
114: [16775299, 1374, 16776956, 2212, 1577, 4993, 1351, 16777040]
122: [16774665, 1498, 16776379, 3062, 1593, 5966, 1924, 16776815]
130: [16774318, 851, 16775763, 3663, 711, 5193, 2591, 16777069]
138: [16774005, 1189, 16776283, 3892, 1372, 6362, 2910, 307]
146: [16775169, 1031, 16776798, 2426, 1171, 4570, 1728, 33]
154: [16775201, 819, 16776898, 2370, 1132, 4255, 1900, 347]
```

> The input should have 64 characters, 8 characters as a chunk, and will undergo some computation before comparing with the target buffer.

### Calculation
Input the flag as `cyclic(64, n=8)` and check the value of the input buffer after the execution.
```bash
> input
16: [16774500, 1164, 16776343, 3298, 1261, 5626, 2328, 0]
24: [16774493, 1162, 16776341, 3307, 1259, 5632, 2337, 5]
32: [16774486, 1160, 16776339, 3316, 1257, 5638, 2346, 10]
40: [16774479, 1158, 16776337, 3325, 1255, 5644, 2355, 15]
48: [16774472, 1156, 16776335, 3334, 1253, 5650, 2364, 20]
56: [16774465, 1154, 16776333, 3343, 1251, 5656, 2373, 25]
64: [16774458, 1152, 16776331, 3352, 1249, 5662, 2382, 30]
72: [16774451, 1150, 16776329, 3361, 1247, 5668, 2391, 35]
```
That is, for each chunk, the difference between the value is the same. Therefore, the computation should just be a simple matrix multiplication.

Also, try input with `hitcon{rhitcon{shitcon{thitcon{uhitcon{vhitcon{whitcon{xhitcon{y`
```bash
> input
16: [16774200, 1411, 16776275, 3646, 1532, 6451, 2510, 16777141]
24: [16774193, 1408, 16776281, 3653, 1536, 6459, 2523, 16777156]
32: [16774186, 1405, 16776287, 3660, 1540, 6467, 2536, 16777171]
40: [16774179, 1402, 16776293, 3667, 1544, 6475, 2549, 16777186]
48: [16774172, 1399, 16776299, 3674, 1548, 6483, 2562, 16777201]
56: [16774165, 1396, 16776305, 3681, 1552, 6491, 2575, 0]
64: [16774158, 1393, 16776311, 3688, 1556, 6499, 2588, 15]
72: [16774151, 1390, 16776317, 3695, 1560, 6507, 2601, 30]
```
All the differece, other than the last one, are the same. Therefore, the computation should still be a matrix multiplication but in a modular field where `16777201 + 15 = 0`. That is, the field is `2^24`.

Therefore, input the following so that the calculated input buffer will be the transformation matrix.
```python
In [11]: [[0 if i != j else 1 for i in range(8)] for j in range(8)]
Out[11]: 
[[1, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 1]]

In [12]: ''.join([''.join(['\0' if i != j else '\1' for i in range(8)]) for j in range(8)])
Out[12]: '\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01'
```

Transformation Matrix:
```bash
> input
16: [16777209, 16777214, 16777214, 9, 16777214, 6, 9, 5]
24: [16777214, 3, 16777212, 3, 2, 7, 16777215, 16777211]
32: [3, 2, 16777213, 16777213, 16777215, 16777214, 16777210, 16777208]
40: [16777212, 5, 16777213, 5, 3, 13, 1, 16777210]
48: [4, 6, 4, 16777210, 6, 5, 16777208, 16777211]
56: [16777203, 16777206, 16777211, 17, 16777208, 1, 22, 15]
64: [16777214, 11, 16777214, 2, 9, 20, 16777210, 16777205]
72: [16777209, 16777213, 6, 7, 4, 8, 13, 15]
```

***Computation***: Matrix Multiplication  
`target = input * transformation_matrix`, in modular field of $2^{24}$
> All matrices are 8x8

## Solution
> solve script [here](./solve.py)

With known target and transformation matrix, use **SMT Solver**, `cvc5`, to solve for the input since the computation is matrix multiplication in a modular field of `2^24`.

### Result
Use `cvc5` to solve the constraints with [script](./solve.py).

```bash
> python3 solve.py
hitcon{r3vErs1ng_0n3_1ns7ruction_vm_1s_Ann0ying_c9adf98b67af517}
```

## Appendix
### Subleq
> [related link](https://esolangs.org/wiki/Subleq)
