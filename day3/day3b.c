#include <stdio.h>
#include <stdlib.h>

int main() {
  FILE* f = fopen("input.txt", "r");
  int length = 12;
  int count = 1000;
  int* O2 = (int*)malloc(sizeof(int) * count);
  int* CO2 = (int*)malloc(sizeof(int) * count);
  for (int i = 0; i < count; i++) {
    int num = 0;
    for (int j = 0; j < length; j++) {
      num <<= 1;
      char bit;
      fscanf(f, "%c", &bit);
      if (bit == '1')
        num++;
    }
    fscanf(f, " ");
    O2[i] = num;
    CO2[i] = num;
  }
  fclose(f);
  
  int remCount = count;
  for (int p = length-1; p >= 0 && remCount > 1; p--) {
    int onbits = 0;
    for (int i = 0; i < remCount; i++) {
      if ((O2[i] >> p) & 1)
        onbits++;
    }
    int* newO2;
    if (onbits*2 >= remCount) {
      newO2 = (int*)malloc(sizeof(int) * onbits);
      for (int i = 0, j = 0; i < remCount, j < onbits; i++) {
        if ((O2[i] >> p) & 1) {
          newO2[j] = O2[i];
          j++;
        }
      }
      remCount = onbits;
    } else {
      newO2 = (int*)malloc(sizeof(int) * (remCount - onbits));
      for (int i = 0, j = 0; i < remCount, j < (remCount - onbits); i++) {
        if (!((O2[i] >> p) & 1)) {
          newO2[j] = O2[i];
          j++;
        }
      }
      remCount -= onbits;
    }
    free(O2);
    O2 = newO2;
  }
  
  remCount = count;
  for (int p = length-1; p >= 0 && remCount > 1; p--) {
    int onbits = 0;
    for (int i = 0; i < remCount; i++) {
      if ((CO2[i] >> p) & 1)
        onbits++;
    }
    int* newCO2;
    if (onbits*2 >= remCount) {
      newCO2 = (int*)malloc(sizeof(int) * (remCount - onbits));
      for (int i = 0, j = 0; i < remCount, j < (remCount - onbits); i++) {
        if (!((CO2[i] >> p) & 1)) {
          newCO2[j] = CO2[i];
          j++;
        }
      }
      remCount -= onbits;
    } else {
      newCO2 = (int*)malloc(sizeof(int) * onbits);
      for (int i = 0, j = 0; i < remCount, j < onbits; i++) {
        if ((CO2[i] >> p) & 1) {
          newCO2[j] = CO2[i];
          j++;
        }
      }
      remCount = onbits;
    }
    free(CO2);
    CO2 = newCO2;
  }
  printf("%d\n", O2[0]*CO2[0]);
  return 0;
}