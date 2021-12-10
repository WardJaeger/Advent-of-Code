#include <stdio.h>

int main() {
  FILE* f = fopen("input.txt", "r");
  const int length = 12;
  int count = 0;
  int onbits[length];
  for (int i = 0; i < length; i++)
    onbits[i] = 0;
  while (!feof(f)) {
    for (int i = 0; i < length; i++) {
      char bit;
      fscanf(f, "%c", &bit);
      if (bit == '1')
        onbits[i]++;
    }
    fscanf(f, " ");
    count++;
  }
  int g = 0, e = 0;
  for (int i = 0; i < length; i++) {
    g *= 2;
    e *= 2;
    if (onbits[i] > count/2)
      g++;
    else e++;
  }
  printf("%d\n", g*e);
  return 0;
}