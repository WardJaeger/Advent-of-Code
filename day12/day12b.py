f = open("input.txt")
connections = [x.strip().split("-") for x in f.readlines()]
f.close()

def findPaths(path, flag):
  if path[-1] == "end":
    return 1
  numPaths = 0
  for x in connections:
    if x[0] == path[-1] and x[1] != "start" and (flag or x[1] != x[1].lower() or x[1] not in path):
      newPath = path.copy()
      newPath.append(x[1])
      if x[1] == x[1].lower() and x[1] in path:
        numPaths += findPaths(newPath, False)
      else:
        numPaths += findPaths(newPath, flag)
    elif x[1] == path[-1] and x[0] != "start" and (flag or x[0] != x[0].lower() or x[0] not in path):
      newPath = path.copy()
      newPath.append(x[0])
      if x[0] == x[0].lower() and x[0] in path:
        numPaths += findPaths(newPath, False)
      else:
        numPaths += findPaths(newPath, flag)
  return numPaths

print(findPaths(["start"], True))