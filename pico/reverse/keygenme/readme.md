# Keygenme
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/276/)

## Description
> Can you get the flag?

## What It Does
Ask for a license key and check whether it is valid.

## Solution
1. Inspect the assembly, `main` function
    ```as
    ...
    0x00005555555554be:  mov    rdx,QWORD PTR [rip+0x2b4b]        # 0x555555558010 <stdin>
    0x00005555555554c5:  lea    rax,[rbp-0x30]
    0x00005555555554c9:  mov    esi,0x25
    0x00005555555554ce:  mov    rdi,rax
    0x00005555555554d1:  call   0x5555555550d0 <fgets@plt>  ; Get input license key
    0x00005555555554d6:  lea    rax,[rbp-0x30]
    0x00005555555554da:  mov    rdi,rax
    0x00005555555554dd:  call   0x555555555209              ; compare function
    0x00005555555554e2:  test   al,al
    0x00005555555554e4:  je     0x5555555554f4
    0x00005555555554e6:  lea    rdi,[rip+0xb35]             ; STRING: That key is valid.
    0x00005555555554ed:  call   0x5555555550c0 <puts@plt>
    0x00005555555554f2:  jmp    0x555555555500
    0x00005555555554f4:  lea    rdi,[rip+0xb3a]             ; STRING: That key is invalid.
    0x00005555555554fb:  call   0x5555555550c0 <puts@plt>
    ...
    ```
    - function `0x555555555209` return 1 if valid key and 0 otherwise
        ```as
        ...
        0x0000555555555411:  mov    rdi,rax
        0x0000555555555414:  call   0x5555555550e0 <strlen@plt>
        0x0000555555555419:  cmp    rax,0x24                    ; check if string of length `0x24`
        0x000055555555541d:  je     0x555555555426
        0x000055555555541f:  mov    eax,0x0
        0x0000555555555424:  jmp    0x555555555475
        0x0000555555555426:  mov    DWORD PTR [rbp-0xb8],0x0    ; idx at (rbp-0xb8)
        0x0000555555555430:  jmp    0x555555555467
        0x0000555555555432:  mov    eax,DWORD PTR [rbp-0xb8]
        0x0000555555555438:  movsxd rdx,eax
        0x000055555555543b:  mov    rax,QWORD PTR [rbp-0xd8]
        0x0000555555555442:  add    rax,rdx
        0x0000555555555445:  movzx  edx,BYTE PTR [rax]
        0x0000555555555448:  mov    eax,DWORD PTR [rbp-0xb8]
        0x000055555555544e:  cdqe   
        0x0000555555555450:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]   ; flag at ($rbp-0x30)
        0x0000555555555455:  cmp    dl,al
        0x0000555555555457:  je     0x555555555460
        0x0000555555555459:  mov    eax,0x0
        0x000055555555545e:  jmp    0x555555555475
        0x0000555555555460:  add    DWORD PTR [rbp-0xb8],0x1
        0x0000555555555467:  cmp    DWORD PTR [rbp-0xb8],0x23
        0x000055555555546e:  jle    0x555555555432
        0x0000555555555470:  mov    eax,0x1
        0x0000555555555475:  mov    rsi,QWORD PTR [rbp-0x8]
        0x0000555555555479:  xor    rsi,QWORD PTR fs:0x28
        0x0000555555555482:  je     0x555555555489
        0x0000555555555484:  call   0x555555555110 <__stack_chk_fail@plt>
        0x0000555555555489:  leave  
        0x000055555555548a:  ret    
        ```
        - check the length of the string and compare the input one by one with string stored at `$rbp-0x30`

2. Run program in `gdb`
    1. `s < <(echo "A")`, to start the program
    2. `b *0x0000555555555419`, set break point before checks
    3. `c`, to continue
    4. `x/s ($rbp-0x30)`, get **flag**

3. Steps mentioned in previous step can automate by [script](./solve.py) to get **flag**