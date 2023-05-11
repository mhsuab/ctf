# breadth
> Event: `picoMini by redpwn`  
> Challenge: [link](https://play.picoctf.org/challenges/220/)

## Description
> Surely this is what people mean when they say "horizontal scaling," right?  
> **TOP SECRET INFO:**  
> Our operatives managed to exfiltrate an in-development version of this challenge, where the function with the real flag had a mistake in it. Can you help us get the flag?

## Solution
Both `breadth.v1` and `breadth.v2` will just print out,
```txt
Dead code? What's that?
Goodbye!
```

## What It Does
1. Check the *strings* of the binaries
    ```txt
    ...
    picoCTF{VhQHm6cqLAera5k3g6TpWY1qQJjsAdvF}
    picoCTF{tTYva1pFAmMsVKPOocYt4rk3aCZ3skax}
    picoCTF{4CfUT1dDz04zaMj9oF1uIAZ8raUANAtw}
    picoCTF{sLGe27ZoFBR6czyH3QIph0ppWH3JR2BC}
    picoCTF{tp5dobX3iLNYlSAIJRVVyXtFVxnCCRKJ}
    picoCTF{L2huETZ1VTaGGj6eeV1zzVHeHsfbCTVv}
    picoCTF{zFMvODYAGZjhSc6fyltrNbFXOQlxKbMW}
    picoCTF{fZQNpC8zNnJGMdYXi0JGmfJkZorb4hfr}
    picoCTF{AVt9v5U0UChJ3QmyJ1YlSttzeEzFh36C}
    picoCTF{zJ3pd9XgY5hgCkFryzhwmEvb5wNSi5ma}
    picoCTF{q4AvLTgkQVEf3Q80TxaYzYDKp7IPSu1V}
    picoCTF{aCndYdDGexJBCmnIoUGsjpWMYyxxfH4D}
    picoCTF{zS6v39rzHh3yMCyZcXwMdWyoE9C57CfQ}
    ...
    ```
    - both contains a lot of strings that look like a valid flag
2. Inspect the assembly of `breadth.v1` and `breadth.v2`, the only different function `<fcnkKTQpF>`
    - `breadth.v1`
        ```as
        0000000000095040 <fcnkKTQpF>:
            95040: 48 c7 44 24 f0 3e c7 1b 04   	mov	qword ptr [rsp - 16], 68929342
            95049: 48 8b 54 24 f0               	mov	rdx, qword ptr [rsp - 16]
            9504e: b8 3a 80 37 d0               	mov	eax, 3493298234
            95053: 48 39 c2                     	cmp	rdx, rax
            95056: 74 08                        	je	0x95060 <fcnkKTQpF+0x20>
            95058: c3                           	ret
            95059: 0f 1f 80 00 00 00 00         	nop	dword ptr [rax]
            95060: 48 8d 3d 91 0e 0c 00         	lea	rdi, [rip + 790161]     # 0x155ef8 <_IO_stdin_used+0x93ef8>
            95067: e9 c4 bf f6 ff               	jmp	0x1030 <puts@plt>
            9506c: 0f 1f 40 00                  	nop	dword ptr [rax]
        ```
    - `breadth.v2`
        ```as
        0000000000095040 <fcnkKTQpF>:
            95040: 48 c7 44 24 f0 3e c7 1b 04   	mov	qword ptr [rsp - 16], 68929342
            95049: 48 8b 44 24 f0               	mov	rax, qword ptr [rsp - 16]
            9504e: 48 3d 3e c7 1b 04            	cmp	rax, 68929342
            95054: 74 0a                        	je	0x95060 <fcnkKTQpF+0x20>
            95056: c3                           	ret
            95057: 66 0f 1f 84 00 00 00 00 00   	nop	word ptr [rax + rax]
            95060: 48 8d 3d 91 0e 0c 00         	lea	rdi, [rip + 790161]     # 0x155ef8 <_IO_stdin_used+0x93ef8>
            95067: e9 c4 bf f6 ff               	jmp	0x1030 <puts@plt>
            9506c: 0f 1f 40 00                  	nop	dword ptr [rax]
        ```
3. Run program in `gdb` to get the correct flag (both `breadth.v1`, `breadth.v2` work)
    1. `b main`
    2. `r`, run the program
    3. `set $rip=(fcnkKTQpF+32)`, jump directly to function `<fcnkKTQpF>` before `put`
    4. `ni`, set up the `rdi` for `put`
    5. `x/s $rdi`, get the **correct flag**

4. Steps mentioned in previous step can automate by [script](./solve.py) to get **flag**