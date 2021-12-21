explodeDepth = 4

class Snailfish:
  def __init__(self, value: int):
    self.value = value
    self.p: Snailfish = None
    self.l: Snailfish = None
    self.r: Snailfish = None

  def copy(self):
    s = Snailfish(self.value)
    if self.value == -1:
      s.l = self.l.copy()
      s.r = self.r.copy()
      s.l.p = s
      s.r.p = s
    return s

  def explode(self, depth: int):
    if depth == 0:
      # move left value
      curr = self.p
      prev = self
      while curr != None and prev is curr.l:
        prev = curr
        curr = curr.p
      if curr != None:
        curr = curr.l
        while curr.value == -1:
          curr = curr.r
        curr.value += self.l.value
      
      # move right value
      curr = self.p
      prev = self
      while curr != None and prev is curr.r:
        prev = curr
        curr = curr.p
      if curr != None:
        curr = curr.r
        while curr.value == -1:
          curr = curr.l
        curr.value += self.r.value

      # replace with 0
      self.l = None
      self.r = None
      self.value = 0
      return True

    if self.l.value == -1:
      if self.l.explode(depth-1):
        return True
    if self.r.value == -1:
      if self.r.explode(depth-1):
        return True

    return False

  def split(self):
    if self.value == -1:
      if self.l.split():
        return True
      if self.r.split():
        return True

    if self.value >= 10:
      self.l = Snailfish(self.value//2)
      self.r = Snailfish(self.value - self.value//2)
      self.l.p = self
      self.r.p = self
      self.value = -1
      return True

    return False

  def magnitude(self):
    if self.value == -1:
      return 3*self.l.magnitude() + 2*self.r.magnitude()
    else:
      return self.value

  def toString(self):
    if self.value == -1:
      string: str = "["
      string += self.l.toString()
      string += ","
      string += self.r.toString()
      string += "]"
      return string
    else:
      return str(self.value)

def parseSnailfish(str):
  if str[0] == "[":
    snailfish = Snailfish(-1)
    depth = 0
    for i in range(1, len(str)-1):
      if str[i] == "," and depth == 0:
        l = parseSnailfish(str[1:i])
        r = parseSnailfish(str[i+1:-1])
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

def add(s1: Snailfish, s2: Snailfish):
  s = Snailfish(-1)
  s.l = s1.copy()
  s.r = s2.copy()
  s.l.p = s
  s.r.p = s
  while True:
    while s.explode(explodeDepth):
      pass
    if not s.split():
      return s

f = open("input.txt")
numbers = [parseSnailfish(x.strip()) for x in f.readlines()]
f.close()

maxSum = 0
for x in numbers:
  for y in numbers:
    if x is not y:
      sum = add(x, y).magnitude()
      if maxSum < sum:
        maxSum = sum

print(maxSum)