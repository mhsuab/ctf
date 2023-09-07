# riscy business
> Event: `picoMini by redpwn`  
> Challenge: [link](https://play.picoctf.org/challenges/222/)

## Description
> Try not to take too many riscs when finding the flag.

## What It Does
> I don't have the system to run the binary. Let's go directly to static analysis.

## Solution
1. Inspect the assembly, `main` function
    ```as
    ...
    0x5555555550a3:      call   0x555555555030 <puts@plt>           ; PRINT: "I heard you wanted to bargain for a flag...\n"
    ...
    0x555555555146:      lea    rdi,[rsp+0x70]
    0x55555555514b:      mov    edx,0x40                            ; read 0x40 items
    0x555555555150:      mov    esi,0x1                             ; read item size of 1 bytes
    0x555555555155:      mov    rax,QWORD PTR [rip+0x2e7c]
    0x55555555515c:      vmovdqa xmm0,XMMWORD PTR [rip+0x104c]
    0x555555555164:      mov    QWORD PTR [rsp+0x40],rdi            ; store user input at [rsp+0x70]
    0x555555555169:      add    rbx,0xa0
    0x555555555170:      vmovdqa XMMWORD PTR [rsp+0x160],xmm0
    0x555555555179:      mov    rcx,QWORD PTR [rax]
    0x55555555517c:      call   0x555555555040 <fread@plt>
    ...
    0x5555555553aa:      mov    rsi,QWORD PTR [rsp+0x40]            ; user input
    0x5555555553af:      mov    edx,0x40
    0x5555555553b4:      mov    rdi,QWORD PTR [rsp+0x48]
    0x5555555553b9:      call   0x555555555060 <memcmp@plt>         ; compare user input with possible flag
    ...
    ```
    - In `main` function, use `memcmp` to compare user input with possible flag
2. Run program in `gdb` to get the possible flag that user input compare to
    1. `b memcmp`
    2. `r < <(python -c "print ('a' * 0x40)")`, input *0x40* bytes to get to `memcmp`
    3. `x/s $rdi`, print out the content user input being compared to, which is the **flag**

3. Steps mentioned in previous step can automate by [script](./solve.py) to get **flag**