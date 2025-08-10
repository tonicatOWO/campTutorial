#include <stdio.h>

int main() {
  int a = 65;
  char c = a;        // 允許不安全轉換
  printf("%c\n", c); // 輸出: A
  return 0;
}
