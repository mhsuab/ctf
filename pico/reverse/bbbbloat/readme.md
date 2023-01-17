# Bbbloat
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/255)

## Description
> Can you get the flag?

## Solution
1. Run `bbbbloat` to test the binary
    ```bash
    $ ./bbbbloat 
    What's my favorite number? 1234
    Sorry, that's not it!
    ```
2. Inspect the assembly, `main` function
    ```as
    ...
    0x555555555446:      lea    rax,[rbp-0x40]                      ; store input @[rbp-0x40]
    0x55555555544a:      mov    rsi,rax
    0x55555555544d:      lea    rdi,[rip+0xbcc]
    0x555555555454:      mov    eax,0x0
    0x555555555459:      call   0x555555555140 <__isoc99_scanf@plt> ; Input favorite number
    ...
    0x5555555554c8:      mov    eax,DWORD PTR [rbp-0x40]
    0x5555555554cb:      cmp    eax,0x86187                         ; **compare input with 0x86187**
    0x5555555554d0:      jne    0x555555555583                      ; jmp to 0x555555555583 if not equal
    0x5555555554d6:      mov    DWORD PTR [rbp-0x3c],0x3078
    0x5555555554dd:      add    DWORD PTR [rbp-0x3c],0x13c29e
    0x5555555554e4:      sub    DWORD PTR [rbp-0x3c],0x30a8
    0x5555555554eb:      shl    DWORD PTR [rbp-0x3c],1
    0x5555555554ee:      mov    eax,DWORD PTR [rbp-0x3c]
    0x5555555554f1:      movsxd rdx,eax
    0x5555555554f4:      imul   rdx,rdx,0x55555556
    0x5555555554fb:      shr    rdx,0x20
    0x5555555554ff:      sar    eax,0x1f
    0x555555555502:      mov    ecx,edx
    0x555555555504:      sub    ecx,eax
    0x555555555506:      mov    eax,ecx
    0x555555555508:      mov    DWORD PTR [rbp-0x3c],eax
    0x55555555550b:      mov    DWORD PTR [rbp-0x3c],0x3078
    0x555555555512:      add    DWORD PTR [rbp-0x3c],0x13c29e
    0x555555555519:      sub    DWORD PTR [rbp-0x3c],0x30a8
    0x555555555520:      shl    DWORD PTR [rbp-0x3c],1
    0x555555555523:      mov    eax,DWORD PTR [rbp-0x3c]
    0x555555555526:      movsxd rdx,eax
    0x555555555529:      imul   rdx,rdx,0x55555556
    0x555555555530:      shr    rdx,0x20
    0x555555555534:      sar    eax,0x1f
    0x555555555537:      mov    esi,edx
    0x555555555539:      sub    esi,eax
    0x55555555553b:      mov    eax,esi
    0x55555555553d:      mov    DWORD PTR [rbp-0x3c],eax
    0x555555555540:      lea    rax,[rbp-0x30]
    0x555555555544:      mov    rsi,rax
    0x555555555547:      mov    edi,0x0
    0x55555555554c:      call   0x555555555249                      ; DECRYPT FLAG
    0x555555555551:      mov    QWORD PTR [rbp-0x38],rax
    0x555555555555:      mov    rdx,QWORD PTR [rip+0x2ab4]
    0x55555555555c:      mov    rax,QWORD PTR [rbp-0x38]
    0x555555555560:      mov    rsi,rdx
    0x555555555563:      mov    rdi,rax
    0x555555555566:      call   0x555555555130 <fputs@plt>          ; PRINT FLAG
    0x55555555556b:      mov    edi,0xa
    0x555555555570:      call   0x5555555550e0 <putchar@plt>
    0x555555555575:      mov    rax,QWORD PTR [rbp-0x38]
    0x555555555579:      mov    rdi,rax
    0x55555555557c:      call   0x5555555550d0 <free@plt>
    0x555555555581:      jmp    0x55555555558f
    0x555555555583:      lea    rdi,[rip+0xa99]                     ; STRING: Sorry, that's not it!
    0x55555555558a:      call   0x5555555550f0 <puts@plt>
    0x55555555558f:      mov    eax,0x0
    0x555555555594:      mov    rdi,QWORD PTR [rbp-0x8]
    0x555555555598:      xor    rdi,QWORD PTR fs:0x28
    0x5555555555a1:      je     0x5555555555a8
    0x5555555555a3:      call   0x555555555110 <__stack_chk_fail@plt>
    0x5555555555a8:      leave  
    0x5555555555a9:      ret    
    ```
    - `0x5555555554cb` compare input with **0x86187**, and ended if not equal
3. Run the program and input, `549255`, as favorite number to get the **flag**