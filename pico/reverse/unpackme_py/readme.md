# unpackme.py
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/314/)

## Description
> Can you get the flag?

## What It Does
Ask for a favorite number and print out "The password is incorrect." or flag based on the input number.

## Solution
1. Inspect the python code
    ```python
    ...
    plain = f.decrypt(payload)
    exec(plain.decode())
    ```
    - decrypt payload and run the script
2. Print the decoded plain text, `plain.decode()`, to know what is run
    ```python
    pw = input('What\'s the password? ')

    if pw == 'batteryhorse':
        print('picoCTF{FLAG}')
    else:
        print('That password is incorrect.')
    ```
    - Get the **flag**!!!
