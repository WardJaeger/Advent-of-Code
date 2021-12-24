tiles = {"H": {"0": "", "1": "", "3": "", "5": "", "7": "", "9": "", "10": ""}, "A": [], "B": [], "C": [], "D": []}

f = open("input.txt")
f.readline()
f.readline()
buffer = f.readline()
tiles["A"].insert(0, buffer[3])
tiles["B"].insert(0, buffer[5])
tiles["C"].insert(0, buffer[7])
tiles["D"].insert(0, buffer[9])
buffer = f.readline()
tiles["A"].insert(0, buffer[3])
tiles["B"].insert(0, buffer[5])
tiles["C"].insert(0, buffer[7])
tiles["D"].insert(0, buffer[9])
f.close()

print(tiles)

def moveEnergy(src, dest, tiles):
  o = ""
  if src[0] == "H":
    o = tiles["H"][src[1:]]
  else:
    o = tiles[src][-1]

  # Move only to hallway or correct room
  if dest[0] != "H" and dest != o:
    return 0
  # Do not move from correct room unless occupied
  if src == o:
    flag = True
    for x in tiles[o]:
      if x != o:
        flag = False
    if flag:
      return 0
  # Do not move to correct room if occupied
  if dest == o:
    flag = False
    for x in tiles[o]:
      if x != o:
        flag = True
    if flag:
      return 0
  
  weight = 0
  if o == "A":
    weight = 1
  elif o == "B":
    weight = 10
  elif o == "C":
    weight = 100
  elif o == "D":
    weight = 1000

  count = 0
  start = -1
  end = -1

  if src[0] == "H":
    start = int(src[1:])
  else:
    if src == "A":
      start = 2
    elif src == "B":
      start = 4
    elif src == "C":
      start = 6
    elif src == "D":
      start = 8

    count += 3-len(tiles[src])

  if dest[0] == "H":
    end = int(dest[1:])
  else:
    if dest == "A":
      end = 2
    elif dest == "B":
      end = 4
    elif dest == "C":
      end = 6
    elif dest == "D":
      end = 8

    count += 2-len(tiles[dest])

  for i in range(end, start, -1 if start < end else 1):
    if str(i) in tiles["H"] and tiles["H"][str(i)] != "":
      return 0
    count += 1
  return count*weight

def copyTiles(tiles):
  newTiles = {}
  for key in tiles:
    newTiles[key] = tiles[key].copy()
  return newTiles

def isDone(tiles):
  for key in tiles:
    if key == "H":
      continue
    if len(tiles[key]) != 2 or tiles[key][0] != key or tiles[key][1] != key:
      return False
  return True

minEnergy = -1
def findEnergyLeft(tiles, currEnergy):
  global minEnergy

  if isDone(tiles):
    minEnergy = currEnergy
    print(minEnergy)
    return

  for key in tiles:
    if key == "H":
      for src in tiles["H"]:
        o = tiles["H"][src]
        if o == "":
          continue
        
        mEnergy = moveEnergy("H"+src, o, tiles)
        if mEnergy and (minEnergy == -1 or currEnergy+mEnergy < minEnergy):
          newTiles = copyTiles(tiles)
          newTiles["H"][src] = ""
          newTiles[o].append(o)
          findEnergyLeft(newTiles, currEnergy+mEnergy)
    elif len(tiles[key]):
      for dest in tiles["H"]:
        mEnergy = moveEnergy(key, "H"+dest, tiles)
        if mEnergy and (minEnergy == -1 or currEnergy+mEnergy < minEnergy):
          newTiles = copyTiles(tiles)
          o = newTiles[key].pop()
          newTiles["H"][dest] = o
          findEnergyLeft(newTiles, currEnergy+mEnergy)

findEnergyLeft(tiles, 0)
print(minEnergy)