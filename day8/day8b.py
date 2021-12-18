f = open("input.txt")
buffer = f.readline()

count = 0
while buffer != "":
  digits = [""] * 10
  fives = []
  sixes = []

  # sort digits by number of segments
  for x in buffer.split("|")[0].strip().split():
    if len(x) == 2:
      digits[1] = sorted(x)
    elif len(x) == 3:
      digits[7] = sorted(x)
    elif len(x) == 4:
      digits[4] = sorted(x)
    elif len(x) == 5:
      fives.append(sorted(x))
    elif len(x) == 6:
      sixes.append(sorted(x))
    elif len(x) == 7:
      digits[8] = sorted(x)

  # determine 3 by comparison to 1
  if digits[1][0] in fives[0] and digits[1][1] in fives[0]:
    digits[3] = fives[0]
    fives.pop(0)
  elif digits[1][0] in fives[1] and digits[1][1] in fives[1]:
    digits[3] = fives[1]
    fives.pop(1)
  else:
    digits[3] = fives[2]
    fives.pop(2)

  # determine 6 by comparison to 1
  if digits[1][0] not in sixes[0] or digits[1][1] not in sixes[0]:
    digits[6] = sixes[0]
    sixes.pop(0)
  elif digits[1][0] not in sixes[1] or digits[1][1] not in sixes[1]:
    digits[6] = sixes[1]
    sixes.pop(1)
  else:
    digits[6] = sixes[2]
    sixes.pop(2)

  # determine 2 and 5 by comparison to 6
  if fives[0][0] in digits[6] and fives[0][1] in digits[6] and fives[0][2] in digits[6] and fives[0][3] in digits[6] and fives[0][4] in digits[6]:
    digits[5] = fives[0]
    digits[2] = fives[1]
  else:
    digits[5] = fives[1]
    digits[2] = fives[0]
  fives = []

  # determine 0 and 9 by comparison to 4
  if digits[4][0] in sixes[0] and digits[4][1] in sixes[0] and digits[4][2] in sixes[0] and digits[4][3] in sixes[0]:
    digits[9] = sixes[0]
    digits[0] = sixes[1]
  else:
    digits[9] = sixes[1]
    digits[0] = sixes[0]
  sixes = []

  outputs = buffer.split("|")[1].strip().split()
  value = 0
  for i in range(len(outputs)):
    value *= 10
    value += digits.index(sorted(outputs[i]))

  count += value
  buffer = f.readline()

f.close()

print(count)