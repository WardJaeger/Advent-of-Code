f = open("input.txt")
buffer = f.readline()
f.close()

groups = []
for x in buffer.strip("\n").split(","):
  while int(x) >= len(groups):
    groups.append(0)
  groups[int(x)] += 1

prevFuel = 0
for i in range(len(groups)):
  prevFuel += i*groups[i]

pos = 1
while True:
  currFuel = 0
  for i in range(len(groups)):
    currFuel += abs(i-pos)*groups[i]
  if (currFuel >= prevFuel):
    print(prevFuel)
    quit()
  prevFuel = currFuel
  pos += 1