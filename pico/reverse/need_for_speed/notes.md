1. b main
2. set $rip=0x0000555555400947
3. step until 0x00005555554008c2
4. set $eax=0xE730FC6F
5. `ni` through function decrypt_flag
6. flag can be found in argument in `puts` 
