# Safe Opener
> Event: `picoCTF 2022`  
> Challenge: [link](https://play.picoctf.org/challenges/294/)

## Description
> Can you open this safe?  
> I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe?  
> Put the password you recover into the picoCTF flag format like:  
> picoCTF{password}

## Solution
1. Inspect the java code
    - check the base64 encoded password and give flag if password matches
    ```java
    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
    ```
2. Input the base64 decoded string of, `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`
    ```bash
    $ echo cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz | base64 -d
    pl3as3_l3t_m3_1nt0_th3_saf3
    ```
3. Construct the password into the **picoCTF flag format**