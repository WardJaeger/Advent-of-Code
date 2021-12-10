#include <stdio.h>

int main() {
  FILE* f = fopen("input.txt", "r");
  int oldVal, newVal, num = 0;
  fscanf(f, "%d ", &oldVal);
  while (!feof(f)) {
    fscanf(f, "%d ", &newVal);
    if (oldVal < newVal) num++;
    oldVal = newVal;
  }
  fclose(f);
  printf("%d\n", num);
  return 0;
}