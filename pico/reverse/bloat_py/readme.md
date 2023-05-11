# bloat.py
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/256/)

## Description
> Can you get the flag?

## What It Does
Ask for password and exit if the password not correct or print out the flag for user.

## Solution
1. Inspect the python code
    - all the strings are obfuscated
    - function `arg133` check for input password and `sys.exit(0)` if not matched
2. nullify `sys.exit(0)` and run the program again
    ```python
    sys.exit = lambda status: print (f'exit({status})')
    ```
    - enter random string for password
3. password incorrect but program still give the **flag**