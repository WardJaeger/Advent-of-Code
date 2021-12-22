f = open("input.txt")
p1Pos = int(f.readline().strip()[-1])
p2Pos = int(f.readline().strip()[-1])
f.close()

weights = [0] * 7
for i in range(1, 4):
  for j in range(1, 4):
    for k in range(1, 4):
      weights[i+j+k - 3] += 1
def weightedAdd(lists: list):
  if len(lists) != 7:
    raise ValueError()
  global weights
  sum = [0] * len(lists[0])
  for i in range(7):
    for j in range(len(sum)):
      sum[j] += lists[i][j]*weights[i]
  return sum

winScore = 21
gottenWins = {}
def getWins(step, p1Score, p2Score, p1Pos, p2Pos, info):
  global winScore, gottenWins
  if step == 0 or step == 2:
    l3 = getWins(step+1, p1Score, p2Score, p1Pos, p2Pos, 3)
    l4 = getWins(step+1, p1Score, p2Score, p1Pos, p2Pos, 4)
    l5 = getWins(step+1, p1Score, p2Score, p1Pos, p2Pos, 5)
    l6 = getWins(step+1, p1Score, p2Score, p1Pos, p2Pos, 6)
    l7 = getWins(step+1, p1Score, p2Score, p1Pos, p2Pos, 7)
    l8 = getWins(step+1, p1Score, p2Score, p1Pos, p2Pos, 8)
    l9 = getWins(step+1, p1Score, p2Score, p1Pos, p2Pos, 9)
    return weightedAdd([l3, l4, l5, l6, l7, l8, l9])
  elif step == 1:
    newPos = (p1Pos+info-1) % 10 + 1
    if p1Score + newPos >= winScore:
      return [1,0]
    else:
      key = str(step) + "," + str(p1Score+newPos) + "," + str(p2Score) + "," + str(newPos) + "," + str(p2Pos)
      if key not in gottenWins:
        gottenWins[key] = getWins(step+1, p1Score+newPos, p2Score, newPos, p2Pos, 0)
      return gottenWins[key]
  elif step == 3:
    newPos = (p2Pos+info-1) % 10 + 1
    if p2Score + newPos >= winScore:
      return [0,1]
    else:
      key = str(step) + "," + str(p1Score) + "," + str(p2Score+newPos) + "," + str(p1Pos) + "," + str(newPos)
      if key not in gottenWins:
        gottenWins[key] = getWins(0, p1Score, p2Score+newPos, p1Pos, newPos, 0)
      return gottenWins[key]
  raise ValueError()
    
wins = getWins(0, 0, 0, p1Pos, p2Pos, 0)
print(max(wins[0], wins[1]))