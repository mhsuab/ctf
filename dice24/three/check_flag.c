#include <stdint.h>
#include <string.h>

int8_t fn_check_if_matched_mem_0toC(int, int);

int delta_Y_list[];
int delta_X_list[];
int indicesB[];
int indicesA[];

typedef int8_t bool;
struct _data {
  int div;
  int mod;
};

int8_t check_flag(struct _data *data) {
  int Y;                // r15d
  unsigned int X;       // ebp
  int v3;               // eax
  int loop_n_idx;       // r8d
  int delta_X;          // r13d
  int64_t prev;         // rbx
  int delta_Y;          // r12d
  int cur;              // eax
  int checker;          // esi
  int v10;              // ecx
  int64_t index;        // rax
  int64_t indexA;       // rsi
  int64_t indexB;       // rax
  int loop_idx;         // [rsp+0h] [rbp-88h]
  int counter;          // [rsp+4h] [rbp-84h]
  int32_t checkers[13]; // [rsp+10h] [rbp-78h] BYREF

  Y = 0;
  X = 0;
  memset(checkers, 0, sizeof(checkers));
  loop_n_idx = 1;
  counter = 0;
  delta_X = -1;
  // prev = fn_check_if_matched_mem_0toC(0, 0);
  prev = 0;
  delta_Y = 0;
  while (1) {
    index = *((int *)data + (int)(Y + 8 * X));
    indexA = indicesA[index];
    indexB = indicesB[index];

    bool A_not_zeroes =
             delta_X_list[indexA] + delta_X || delta_Y_list[indexA] + delta_Y,
         B_not_zeroes =
             delta_X_list[indexB] + delta_X || delta_Y_list[indexB] + delta_Y;
    if (A_not_zeroes && B_not_zeroes) {
      return 0;
    } else if (A_not_zeroes) {
      delta_Y = delta_Y_list[indexA];
      delta_X = delta_X_list[indexA];
    } else {
      delta_Y = delta_Y_list[indexB];
      delta_X = delta_X_list[indexB];
    }
    loop_idx = loop_n_idx;
    cur = fn_check_if_matched_mem_0toC(X, Y);
    if (((unsigned int)prev & cur) != -1) {
      if (cur == (int32_t)prev) {
        // NOTE: max consecutive should be 3
        if (++counter > 3)
          return 0LL;
      } else {
        // NOTE: update checkers value if counter is larger
        checker = checkers[prev];
        v10 = counter;
        counter = 1;
        if (checker < v10)
          checker = v10;
        checkers[prev] = checker;
      }
    }
    X += delta_X;
    Y += delta_Y;
    // if ((unsigned int)(loop_idx - 1) > 62)
    if (loop_idx > 63)
      break;
    // if (!(Y | X)) // NOTE: return 0 if (X == 0 and Y == 0)
    if ((X == 0) && (Y == 0))
      return 0LL;
    loop_n_idx = loop_idx + 1;
    // if ((Y | X) > 7)
    if ((Y > 7) || (X > 7))
      return 0LL;
  LABEL_13:
    prev = cur;
  }
  if (loop_idx != 0x80) {
    loop_n_idx = loop_idx + 1;
    // if ((Y | X) > 7)
    if ((Y > 7) || (X > 7))
      return 0LL;
    goto LABEL_13;
  }
  return checkers[0] == 3 && checkers[1] == 3 && checkers[2] == 3 &&
         checkers[3] == 3 && checkers[4] == 3 && checkers[5] == 3 &&
         checkers[6] == 3 && checkers[7] == 3 && checkers[8] == 3 &&
         checkers[9] == 3 && checkers[10] == 3 && checkers[11] == 3 &&
         checkers[12] == 3;
}
