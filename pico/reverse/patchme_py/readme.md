# patchme.py
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/287/)

## Description
> Can you get the flag?  
> Run this Python program in the same directory as this encrypted flag.

## Solution
1. Inspect the python code
    ```python
    def level_1_pw_check():
        user_pw = input("Please enter correct password for flag: ")
        if( user_pw == "ak98" + \
                    "-=90" + \
                    "adfjhgj321" + \
                    "sleuth9000"):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), "utilitarian")
            print(decryption)
            return
        print("That password is incorrect")
    ```
    - program ask for password and pass the check for correct password
2. However, the `user_pw` does not affect the decryption.
3. Remove the check for password and run it directly to get the *flag*