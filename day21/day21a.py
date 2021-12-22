dieValue = 1
def rollDie():
  global dieValue
  prevValue = dieValue
  dieValue = (dieValue%100) + 1
  return prevValue

f = open("input.txt")
p1Pos = int(f.readline().strip()[-1])
p2Pos = int(f.readline().strip()[-1])
f.close

p1Score = 0
p2Score = 0
rollCount = 0

while True:
  step = rollDie() + rollDie() + rollDie()
  rollCount += 3
  p1Pos = (p1Pos+step-1) % 10 + 1
  p1Score += p1Pos
  if p1Score >= 1000:
    print(p2Score * rollCount)
    quit()
    
  step = rollDie() + rollDie() + rollDie()
  rollCount += 3
  p2Pos = (p2Pos+step-1) % 10 + 1
  p2Score += p2Pos
  if p2Score >= 1000:
    print(p1Score * rollCount)
    quit()