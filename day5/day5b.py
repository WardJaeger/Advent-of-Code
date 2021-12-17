grid = []
def addToGrid(row, col):
  while row >= len(grid):
    grid.append([])
  while col >= len(grid[row]):
    grid[row].append(0)
  grid[row][col] += 1

f = open("input.txt")
bufferLine = f.readline().strip("\n")

while bufferLine != "":
  points = bufferLine.split(" -> ")
  start = [int(x) for x in points[0].split(",")] 
  end = [int(x) for x in points[1].split(",")] 
  if start[0] == end[0]:
    if start[1] <= end[1]:
      for y in range(start[1], end[1]+1):
        addToGrid(y, start[0])
    else:
      for y in range(end[1], start[1]+1):
        addToGrid(y, start[0])
  elif start[1] == end[1]:
    if start[0] <= end[0]:
      for x in range(start[0], end[0]+1):
        addToGrid(start[1], x)
    else:
      for x in range(end[0], start[0]+1):
        addToGrid(start[1], x)
  elif start[0] <= end[0]:
    for i in range(end[0]-start[0]+1):
      if start[1] <= end[1]:
        addToGrid(start[1]+i, start[0]+i)
      else:
        addToGrid(start[1]-i, start[0]+i)
  else:
    for i in range(start[0]-end[0]+1):
      if start[1] <= end[1]:
        addToGrid(end[1]-i, end[0]+i)
      else:
        addToGrid(end[1]+i, end[0]+i)      
  bufferLine = f.readline().strip("\n")

f.close()

count = 0
for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] > 1:
      count += 1
print(count)