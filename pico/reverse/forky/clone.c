#include <stdio.h>
#include <sys/mman.h>
#include <unistd.h>

int main() {
    int * addr = (int *)mmap(0, 4, 3, 33, -1, 0);
    int * count = (int *)mmap(0, 4, 3, 33, -1, 0);
    *addr = 1000000000;
    *count = 0;
    fork();
    fork();
    fork();
    fork();
    *addr += 1234567890;
    *count += 1;
    printf ("%d:\t%d\n", *count, *addr);
    return 0;
}