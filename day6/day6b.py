f = open("input.txt")
ages = f.readline().strip("\n")
f.close()

groups = [0] * 9
for x in ages.split(","):
  groups[int(x)] += 1

for _ in range(256):
  newGroups = [0] * 9
  for i in range(len(groups)):
    if i == 0:
      newGroups[6] += groups[i]
      newGroups[8] += groups[i]
    else:
      newGroups[i-1] += groups[i]
  groups = newGroups

count = 0
for x in groups:
  count += x
print(count)