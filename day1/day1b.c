#include <stdio.h>

int main() {
  FILE* f = fopen("input.txt", "r");
  int a, b, c, d, num = 0;
  fscanf(f, "%d %d %d ", &a, &b, &c);
  while (!feof(f)) {
    fscanf(f, "%d ", &d);
    if (a < d) num++;
    a = b;
    b = c;
    c = d;
  }
  fclose(f);
  printf("%d\n", num);
  return 0;
}