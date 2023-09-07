       LEA      RSI,[s_Give_me_the_flag:_00402000]          = "Give me the flag: "
       MOV      EDI,0x1                                     fd = stdout
       MOV      EDX,0x12                                    count
       MOV      EAX,0x1
       SYSCALL                                              sys_write(stdout, "Give me the flag: ", 0x12)
       XOR      EDI,EDI
       MOV      RSI,INPUT                                     char* buf
       MOV      EDX,0x64                                    count
       XOR      EAX,EAX
       SYSCALL                                              sys_read(stdin, [INPUT], 0x64)
       CMP      INPUT_LENGTH,0x40                                    RAX = length of input
       JNZ      fail                                        fail if input != 0x40
       XOR      R_CHECK_FAIL_IF_NOT_0,R_CHECK_FAIL_IF_NOT_0
       LEA      R11,[DAT_0040203c]                          = 06h
       XOR      IDX,IDX

[0x40103b]
LAB_LOOP                                        XREF[1]:     00401071(j)  
       CMP      IDX,INPUT_LENGTH
       JGE      END_LOOP
       MOVZX    R9,byte ptr [INPUT + IDX*0x1]=>local_res0
       MOV      R8,qword ptr [DAT_0040203c + R9*0x8]        = 06h
       ROL      R8,0x8
       MOVZX    R13,R8B
       XOR      R14,R14
LAB_00401058                                    XREF[1]:     00401069(j)  
       CMP      R14,R13
       JGE      fail_inc_r_check
       ROL      R8,0x8
       CMP      R8B,IDX_B
       JZ       LOOP_NEXT
       INC      R14
       JMP      LAB_00401058
[0x40106b]
fail_inc_r_check                                XREF[1]:     0040105b(j)  
       INC      R_CHECK_FAIL_IF_NOT_0
[0x40106e]
LOOP_NEXT                                    XREF[1]:     00401064(j)  
       INC      IDX
       JMP      LAB_LOOP
END_LOOP                                        XREF[1]:     0040103e(j)  
       TEST     R_CHECK_FAIL_IF_NOT_0,R_CHECK_FAIL_IF_NOT_0
       JNZ      fail
       JMP      flag
       ??       EBh
       ??       00h

flag                                             XREF[1]:     00401078(j)  
       LEA      RSI,[s_That_was_the_flag!_0040202a]         = "That was the flag!"
       MOV      EDX,0x12
       JMP      LAB_0040109a
fail                                            XREF[2]:     0040102b(j), 00401076(j)  
       LEA      RSI,[s_That_was_not_the_flag_:(_00402012]   = "That was not the flag :("
       MOV      EDX,0x18
       JMP      LAB_0040109a
LAB_0040109a                                    XREF[2]:     00401089(j), 00401098(j)  
       MOV      EDI,0x1
       MOV      EAX,0x1
       SYSCALL                                  sys_write(stdout, ) // print buf from `string` or `fail`
       PUSH     0xa
       MOV      RSI,RSP
       MOV      EDX,0x1
       MOV      EAX,0x1
       SYSCALL                                  sys_write(stdout, "\n", 0x1)
       XOR      EDI,EDI
       MOV      RAX,0x3c
       SYSCALL                                  sys_exit(0)
