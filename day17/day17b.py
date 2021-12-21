f = open("input.txt")
buffer = f.readline().strip()
f.close()

xRange = [int(x) for x in buffer.split()[2].strip("x=,").split("..")]
yRange = [int(y) for y in buffer.split()[3].strip("y=").split("..")]
def isInRange(x, y):
  return x >= xRange[0] and x <= xRange[1] and y >= yRange[0] and y <= yRange[1]
def isPastRange(x, y):
  return x > xRange[1] or y < yRange[0]

xVelRange = [1, xRange[1]+1]
yVelRange = [yRange[0], abs(yRange[0])-1]

count = 0
for yVel0 in range(yVelRange[0], yVelRange[1]+1):
  for xVel0 in range(xVelRange[0], xVelRange[1]+1):
    x = 0
    y = 0
    xVel = xVel0
    yVel = yVel0
    while not isPastRange(x, y):
      x += xVel
      y += yVel
      if xVel != 0:
        xVel -= 1
      yVel -= 1
      if isInRange(x, y):
        count += 1
        break

print(count)