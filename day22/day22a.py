f = open("input.txt")
steps = []
buffer = f.readline().strip()
while buffer != "":
  step = []
  step.append(buffer.split()[0] == "on")
  step.extend(buffer.split()[1].split(",")[0].strip("x=").split(".."))
  step.extend(buffer.split()[1].split(",")[1].strip("y=").split(".."))
  step.extend(buffer.split()[1].split(",")[2].strip("z=").split(".."))
  step = [int(x) for x in step]
  steps.append(step)
  buffer = f.readline().strip()
f.close()

grid = []
for x in range(101):
  grid.append([])
  for y in range(101):
    grid[x].append([0] * 101)

for step in steps:
  state = step[0]
  for x in range(max(step[1]+50, 0), min(step[2]+50+1, 101)):
    for y in range(max(step[3]+50, 0), min(step[4]+50+1, 101)):
      for z in range(max(step[5]+50, 0), min(step[6]+50+1, 101)):
        grid[x][y][z] = state

count = 0
for x in range(101):
  for y in range(101):
    for z in range(101):
      count += grid[x][y][z]
print(count)