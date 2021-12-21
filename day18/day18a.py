class Snailfish:
  def __init__(self, value: int):
    self.value = value
    self.p: Snailfish = None
    self.l: Snailfish = None
    self.r: Snailfish = None
    
def convertToSnailfish(str):
  if str[0] == "[":
    snailfish = Snailfish(-1)
    depth = 0
    for i in range(1, len(str)-1):
      if str[i] == "," and depth == 0:
        l = convertToSnailfish(str[1:i])
        r = convertToSnailfish(str[i+1:-1])
        snailfish.l = l
        snailfish.r = r
        l.p = snailfish
        r.p = snailfish
        return snailfish
      if str[i] == "[":
        depth += 1
      elif str[i] == "]":
        depth -= 1
    raise ValueError
  else:
    return Snailfish(int(str))

def convertToString(snailfish: Snailfish):
  if snailfish.value == -1:
    string: str = "["
    string += convertToString(snailfish.l)
    string += ","
    string += convertToString(snailfish.r)
    string += "]"
    return string
  else:
    return str(snailfish.value)

f = open("input.txt")
numbers = [convertToSnailfish(x.strip()) for x in f.readlines()]
f.close()

def explode(snailfish: Snailfish, depth: int):
  if depth == 4:
    # move left value
    curr = snailfish.p
    prev = snailfish
    while curr != None and prev is curr.l:
      prev = curr
      curr = curr.p
    if curr != None:
      curr = curr.l
      while curr.value == -1:
        curr = curr.r
      curr.value += snailfish.l.value
    
    # move right value
    curr = snailfish.p
    prev = snailfish
    while curr != None and prev is curr.r:
      prev = curr
      curr = curr.p
    if curr != None:
      curr = curr.r
      while curr.value == -1:
        curr = curr.l
      curr.value += snailfish.r.value

    # replace with 0
    snailfish.l = None
    snailfish.r = None
    snailfish.value = 0
    return True

  if snailfish.l.value == -1:
    if explode(snailfish.l, depth+1):
      return True
  if snailfish.r.value == -1:
    if explode(snailfish.r, depth+1):
      return True

  return False

def split(snailfish: Snailfish):
  if snailfish.value == -1:
    if split(snailfish.l):
      return True
    if split(snailfish.r):
      return True

  if snailfish.value >= 10:
    snailfish.l = Snailfish(snailfish.value//2)
    snailfish.r = Snailfish(snailfish.value - snailfish.value//2)
    snailfish.l.p = snailfish
    snailfish.r.p = snailfish
    snailfish.value = -1
    return True

  return False

def reduce(snailfish: Snailfish):
  while True:
    while explode(snailfish, 0):
      pass
    if not split(snailfish):
      return

def add(s1: Snailfish, s2: Snailfish):
  s = Snailfish(-1)
  s.l = s1
  s.r = s2
  s1.p = s
  s2.p = s
  reduce(s)
  return s

def magnitude(snailfish: Snailfish):
  if snailfish.value == -1:
    return 3*magnitude(snailfish.l) + 2*magnitude(snailfish.r)
  else:
    return snailfish.value

sum = numbers[0]
for i in range(1, len(numbers)):
  sum = add(sum, numbers[i])

print(convertToString(sum))
print(magnitude(sum))