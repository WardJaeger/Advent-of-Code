f = open("input.txt")
messages = f.read()
f.close()

index = 0
bit = 0
def getValue(number):
  global index, bit
  value = 0
  for _ in range(number):
    byte = bin(int(messages[index], base=16))[2:].zfill(4)
    value *= 2
    if (byte[bit] == "1"):
      value += 1
    if bit == 3:
      bit = 0
      index += 1
    else:
      bit += 1
  return value
def getPosition():
  global index, bit
  return 4*index + bit

versionSum = 0
def readPacket():
  global versionSum
  versionSum += getValue(3)
  if getValue(3) == 4:
    while getValue(1):
      getValue(4)
    getValue(4)
  else:
    if getValue(1):
      numSubpackets = getValue(11) 
      for _ in range(numSubpackets):
        readPacket()
    else:
      lengthSubpackets = getValue(15)
      startPosition = getPosition()
      while getPosition() < startPosition + lengthSubpackets:
        readPacket()

readPacket()
print(versionSum)