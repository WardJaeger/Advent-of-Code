f = open("input.txt")
risks = [[int(y) for y in x.strip()] for x in f.readlines()]
f.close()

size = len(risks)
for time in range(4):
  for i in range(size):
    for j in range(size):
      risks[i].append((risks[i][j] + time) % 9 + 1)
for time in range(4):
  for i in range(size):
    risks.append([])
    for j in range(size*5):
      risks[-1].append((risks[i][j] + time) % 9 + 1)

pathRisks = []
for i in range(len(risks)):
  pathRisks.append([-1] * len(risks[0]))
pathRisks[0][0] = 0

nextSquares = [[0, 0]]

def findPathRisks(i, j):
  if i != len(risks)-1 and (pathRisks[i+1][j] == -1 or pathRisks[i+1][j] > risks[i+1][j] + pathRisks[i][j]):
    pathRisks[i+1][j] = risks[i+1][j] + pathRisks[i][j]
    nextSquares.append([i+1, j])
  if j != len(risks[0])-1 and (pathRisks[i][j+1] == -1 or pathRisks[i][j+1] > risks[i][j+1] + pathRisks[i][j]):
    pathRisks[i][j+1] = risks[i][j+1] + pathRisks[i][j]
    nextSquares.append([i, j+1])
  if i != 0 and (pathRisks[i-1][j] == -1 or pathRisks[i-1][j] > risks[i-1][j] + pathRisks[i][j]):
    pathRisks[i-1][j] = risks[i-1][j] + pathRisks[i][j]
    nextSquares.append([i-1, j])
  if j != 0 and (pathRisks[i][j-1] == -1 or pathRisks[i][j-1] > risks[i][j-1] + pathRisks[i][j]):
    pathRisks[i][j-1] = risks[i][j-1] + pathRisks[i][j]
    nextSquares.append([i, j-1])

while len(nextSquares):
  next = nextSquares.pop(0)
  findPathRisks(next[0], next[1])

print(pathRisks[len(pathRisks)-1][len(pathRisks[0])-1])