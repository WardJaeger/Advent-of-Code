f = open("input.txt")
connections = [x.strip().split("-") for x in f.readlines()]
f.close()

def findPaths(path):
  if path[-1] == "end":
    return 1
  numPaths = 0
  for x in connections:
    if x[0] == path[-1] and (x[1] != x[1].lower() or x[1] not in path):
      newPath = path.copy()
      newPath.append(x[1])
      numPaths += findPaths(newPath)
    elif x[1] == path[-1] and (x[0] != x[0].lower() or x[0] not in path):
      newPath = path.copy()
      newPath.append(x[0])
      numPaths += findPaths(newPath)
  return numPaths

print(findPaths(["start"]))