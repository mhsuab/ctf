# Fresh Java
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/271/)

## Description
> Can you get the flag?

## What It Does
Ask for key and check the user input to print "Invalid key" or "Valid Key".

## Solution
1. Inspect the java code
    - Compare each characters with hard coded character one by one
    - Check key(flag) with the length of 34
2. Write a [script](./KeygenMe.py) to combine the characters to string