dots = []

f = open("input.txt")
buffer = f.readline()
while buffer.strip() != "":
  dots.append([int(x) for x in buffer.strip().split(",")])
  buffer = f.readline()
  
buffer = f.readline()
while buffer != "":
  parameters = buffer.strip().split()[2].split("=")
  if parameters[0] == "x":
    for x in dots:
      if x[0] > int(parameters[1]):
        x[0] = 2 * int(parameters[1]) - x[0]
  if parameters[0] == "y":
    for x in dots:
      if x[1] > int(parameters[1]):
        x[1] = 2 * int(parameters[1]) - x[1]
  buffer = f.readline()
f.close()

result = []
for x in dots:
  while x[1] >= len(result):
    result.append([])
  while x[0] >= len(result[x[1]]):
    result[x[1]].append(" ")
  result[x[1]][x[0]] = "#"

for x in result:
  string = ""
  for y in x:
    string += y
  print(string)