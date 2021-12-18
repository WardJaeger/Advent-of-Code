f = open("input.txt")
floorMap = [[int(y) for y in x.strip()] for x in f.readlines()]
f.close()

def measureBasin(i, j, done):
  if (done == None):
    done = []

  if floorMap[i][j] == 9 or [i, j] in done:
    return 0
  num = 1
  done.append([i, j])

  if i != 0:
    num += measureBasin(i-1, j, done)
  if j != 0:
    num += measureBasin(i, j-1, done)
  if i != len(floorMap)-1:
    num += measureBasin(i+1, j, done)
  if j != len(floorMap[i])-1:
    num += measureBasin(i, j+1, done)
  
  return num

basins = []
for i in range(len(floorMap)):
  for j in range(len(floorMap)):
    height = floorMap[i][j]
    if (i == 0 or height < floorMap[i-1][j]) and (j == 0 or height < floorMap[i][j-1]) and (i == len(floorMap)-1 or height < floorMap[i+1][j]) and (j == len(floorMap[i])-1 or height < floorMap[i][j+1]):
      basins.append(measureBasin(i, j, None))

basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])