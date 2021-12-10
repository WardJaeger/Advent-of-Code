#include <stdio.h>
#include <string.h>

int main() {
  FILE* f = fopen("input.txt", "r");
  char direction[10];
  int x = 0, y = 0, aim = 0;
  while (!feof(f)) {
    char direction[10];
    int size;
    fscanf(f, "%s %d ", &direction, &size);
    if (!strcmp(direction, "forward")) {
      x += size;
      y += aim*size;
    } else if (!strcmp(direction, "up")) 
      aim -= size;
    else if (!strcmp(direction, "down")) 
      aim += size;
  }
  printf("%d\n", x*y);
  return 0;
}