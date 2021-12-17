f = open("input.txt")
ages = f.readline().strip("\n")
f.close()

ages = [int(x) for x in ages.split(",")]

for _ in range(80):
  size = len(ages)
  for i in range(size):
    if ages[i] == 0:
      ages[i] = 6
      ages.append(8)
    else:
      ages[i] -= 1

print(len(ages))