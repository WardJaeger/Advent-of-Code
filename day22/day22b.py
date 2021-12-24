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

# The uncontrolled area is the amount of cubes affected by some given steps that are later affected by different given step
# The uncontrolled area of steps R by step S equals the area of R and S, minus the uncontrolled area of R and S possessed by each following step
# e.g. Uof1by2 = Aof12 - Uof12by3 - Uof12by4 - Uof12by5 - ...
def getUncontrolledArea(insideIndices, controllingIndex):
  # Get all the necessary steps
  global steps
  insideSteps = []
  for i in insideIndices:
    insideSteps.append(steps[i])
  controllingStep = steps[controllingIndex]

  # Calculate area of insideSteps and controllingStep
  minX = max(max([x[1] for x in insideSteps]), controllingStep[1])
  maxX = min(min([x[2] for x in insideSteps]), controllingStep[2])
  minY = max(max([x[3] for x in insideSteps]), controllingStep[3])
  maxY = min(min([x[4] for x in insideSteps]), controllingStep[4])
  minZ = max(max([x[5] for x in insideSteps]), controllingStep[5])
  maxZ = min(min([x[6] for x in insideSteps]), controllingStep[6])
  if minX > maxX or minY > maxY or minZ > maxZ:
    return 0
  area = (maxX-minX+1) * (maxY-minY+1) * (maxZ-minZ+1)

  # Subtract uncontrolled area of insideSteps and controllingStep, controlled by each subsequent step
  for i in range(controllingIndex+1, len(steps)):
    area -= getUncontrolledArea(insideIndices + [controllingIndex], i)
    if area == 0:
      return 0
  return area

# The controlled area is the amount of cubes that are last affected by a given step.
# The controlled area of step S equals the area of S, minus the uncontrolled area of S possessed by each following step
# e.g. Cof1 = Aof1 - Uof1by2 - Uof1by3 - Uof1by4 - ...
def getControlledArea(index):
  global steps

  # Get area of indexed step
  x = steps[index][2] - steps[index][1] + 1
  y = steps[index][4] - steps[index][3] + 1
  z = steps[index][6] - steps[index][5] + 1
  area = x*y*z

  # Subtract uncontrolled area of indexed step, controlled by each subsequent step
  for i in range(index+1, len(steps)):
    area -= getUncontrolledArea([index], i)
    if area == 0:
      return 0
  return area

count = 0

# There is a lot of overlap in the initialization steps, so it's faster to count the on cubes manually
# We can assume that the later steps do not affect the initialization area
initializationSteps = 20
grid = set()
for i in range(initializationSteps):
  # print(i)
  if steps[i][0]:
    for x in range(steps[i][1], steps[i][2]+1):
      for y in range(steps[i][3], steps[i][4]+1):
        for z in range(steps[i][5], steps[i][6]+1):
          grid.add(str(x)+","+str(y)+","+str(z))
  else:
    for x in range(steps[i][1], steps[i][2]+1):
      for y in range(steps[i][3], steps[i][4]+1):
        for z in range(steps[i][5], steps[i][6]+1):
          grid.discard(str(x)+","+str(y)+","+str(z))
count += len(grid)

# The rest of the steps cover huge areas of memory, so it's faster to calculate the total area that each step controls
for i in range(initializationSteps, len(steps)):
  # print(i)
  if steps[i][0]:
    count += getControlledArea(i)

print(count)