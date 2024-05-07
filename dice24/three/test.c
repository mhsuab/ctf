#include <stdint.h>
#include <stdio.h>

uint64_t table[13] = {
    0x000000000000000f, 0x0000000000101030, 0x000000000000e0c0,
    0x0000000002060200, 0x000000001c080c00, 0x00000000e0e00000,
    0x0002020700000000, 0x0000007800000000, 0x0301010000000000,
    0x0c040c0000000000, 0x0000f00000000000, 0x1038000000000000,
    0xe080000000000000};

int64_t cal(int X, int Y) {
  uint64_t val = 1L << (8 * X + Y);
  if ((table[0] & val) != 0)
    return 0;
  if ((table[1] & val) != 0)
    return 1;
  if ((table[2] & val) != 0)
    return 2;
  if ((table[3] & val) != 0)
    return 3;
  if ((table[4] & val) != 0)
    return 4;
  if ((table[5] & val) != 0)
    return 5;
  if ((table[6] & val) != 0)
    return 6;
  if ((table[7] & val) != 0)
    return 7;
  if ((table[8] & val) != 0)
    return 8;
  if ((table[9] & val) != 0)
    return 9;
  if ((table[10] & val) != 0)
    return 10;
  if ((table[11] & val) != 0)
    return 11;
  return (table[12] & val) == 0 ? -1 : 12;
}

int main() {
  for (int X = 0; X < 8; ++X) {
    for (int Y = 0; Y < 8; ++Y) {
      // printf("(%d, %d): %ld,\n", X, Y, cal(X, Y));
      printf("%ld\t", cal(X, Y));
    }
    printf("\n");
  }
  return 0;
}
