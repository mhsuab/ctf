[cheat sheet](https://acmelabs-galleries.s3.amazonaws.com/48/0000/2352/forensic_cheatsheet.pdf)

- `mmls [disk]`
  - display layout
- `fsstat -o [offset] [disk]`
  - details
- `fls`

**002** mount at `/mnt/boot`, **004** mount at `/`
-> **004** seems more interesting

`fls` to list root directory
-> look into `/root/my_folder`

`icat` to get the content of `/root/my_folder/flag.uni.txt`