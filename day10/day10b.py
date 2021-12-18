f = open("input.txt")

def isOpeningChar(openingChar):
  return openingChar == '(' or openingChar == '[' or openingChar == '{' or openingChar == '<'

def getClosingChar(openingChar):
  if openingChar == '(':
    return ')'
  if openingChar == '[':
    return ']'
  if openingChar == '{':
    return '}'
  if openingChar == '<':
    return '>'

def score(closingChar):
  if closingChar == ')':
    return 1
  if closingChar == ']':
    return 2
  if closingChar == '}':
    return 3
  if closingChar == '>':
    return 4

buffer = f.readline()
autoScores = []
while buffer != "":
  openingChars = []
  flag = True
  for x in buffer.strip():
    if isOpeningChar(x):
      openingChars.append(x)
    elif x == getClosingChar(openingChars[-1]):
      openingChars.pop()
    else:
      flag = False
      break
  if flag:
    currScore = 0
    while len(openingChars):
      currScore *= 5
      currScore += score(getClosingChar(openingChars.pop()))
    autoScores.append(currScore)
  buffer = f.readline()

f.close()

autoScores.sort()
print(autoScores[(len(autoScores)-1)//2])