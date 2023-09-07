#!/bin/bash

cp question.pdf Flag.sh
sh Flag.sh
ar -x flag
mv flag flag.cpio
cpio -idv < flag.cpio
bzip2 -d flag
mv flag.out flag.gz
gzip -d flag.gz
lzip -d flag
mv flag.out flag.lz4
lz4 -d flag.lz4
mv flag flag.xz
lzma -d flag.xz
mv flag flag.lzo
lzop -d flag.lzo
lzip -d flag
mv flag.out flag.xz
xz -d flag.xz
cat flag | xxd -r -p
rm flag*