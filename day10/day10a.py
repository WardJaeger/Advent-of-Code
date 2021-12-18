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
    return 3
  if closingChar == ']':
    return 57
  if closingChar == '}':
    return 1197
  if closingChar == '>':
    return 25137

buffer = f.readline()
errorScore = 0
while buffer != "":
  openingChars = []
  for x in buffer.strip():
    if isOpeningChar(x):
      openingChars.append(x)
    elif x == getClosingChar(openingChars[-1]):
      openingChars.pop()
    else:
      errorScore += score(x)
      break
  buffer = f.readline()

f.close()
print(errorScore)