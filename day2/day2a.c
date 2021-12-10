#include <stdio.h>
#include <string.h>

int main() {
  FILE* f = fopen("input.txt", "r");
  char direction[10];
  int x = 0, y = 0;
  while (!feof(f)) {
    char direction[10];
    int size;
    fscanf(f, "%s %d ", &direction, &size);
    if (!strcmp(direction, "forward")) 
      x += size;
    else if (!strcmp(direction, "up")) 
      y -= size;
    else if (!strcmp(direction, "down")) 
      y += size;
  }
  printf("%d\n", x*y);
  return 0;
}