f = open("input.txt")
floorMap = [[int(y) for y in x.strip()] for x in f.readlines()]
f.close()

riskSum = 0
for i in range(len(floorMap)):
  for j in range(len(floorMap)):
    height = floorMap[i][j]
    if (i == 0 or height < floorMap[i-1][j]) and (j == 0 or height < floorMap[i][j-1]) and (i == len(floorMap)-1 or height < floorMap[i+1][j]) and (j == len(floorMap[i])-1 or height < floorMap[i][j+1]):
      riskSum += height + 1

print(riskSum)