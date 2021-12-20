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
  versionSum += getValue(3) # version number
  typeID = getValue(3)
  if typeID == 4: # literal value
    number = 0
    while getValue(1):
      number *= 16
      number += getValue(4)
    number *= 16
    number += getValue(4)
    return number
  elif typeID < 4: # 1+ subpacket operator
    number = 0
    if typeID == 1: # product operator
      number = 1
    elif typeID == 2 or typeID == 3: # min/max operators
      number = -1

    lengthTypeID = getValue(1)
    limit = 0
    count = 0
    if lengthTypeID: # number of subpackets
      limit = getValue(11)
    else: # total length of subpackets
      limit = getValue(15) + getPosition()
      count = getPosition()

    while count < limit:
      packetNumber = readPacket()
      if typeID == 0: # sum operator
        number += packetNumber
      elif typeID == 1: # product operator
        number *= packetNumber
      elif typeID == 2: # min operator
        if number == -1 or number > packetNumber:
          number = packetNumber
      elif typeID == 3: # max operator
        if number == -1 or number < packetNumber:
          number = packetNumber

      if lengthTypeID: # number of subpackets
        count += 1
      else: # total length of subpackets
        count = getPosition()

    return number
  else: # 2 subpacket operator
    if getValue(1): # number of subpackets
      getValue(11)
    else: # total length of subpackets
      getValue(15)

    number1 = readPacket()
    number2 = readPacket()

    if typeID == 5: # greater than operator
      return int(number1 > number2)
    elif typeID == 6: # less than operator
      return int(number1 < number2)
    elif typeID == 7: # equal to operator
      return int(number1 == number2)

  raise ValueError()

print(readPacket())