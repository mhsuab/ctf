.intel_syntax noprefix
.global asm2

asm2:
	push   ebp
	mov    ebp,esp
	sub    esp,0x10
	mov    eax,DWORD PTR [ebp+0xc]
	mov    DWORD PTR [ebp-0x4],eax
	mov    eax,DWORD PTR [ebp+0x8]
	mov    DWORD PTR [ebp-0x8],eax
	jmp    asm2_28
asm2_20:
	add    DWORD PTR [ebp-0x4],0x1
	sub    DWORD PTR [ebp-0x8],0xffffff80
asm2_28:
	cmp    DWORD PTR [ebp-0x8],0x63f3
	jle    asm2_20
	mov    eax,DWORD PTR [ebp-0x4]
	leave  
	ret    

