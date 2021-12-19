dots = []

f = open("input.txt")
buffer = f.readline()
while buffer.strip() != "":
  dots.append([int(x) for x in buffer.strip().split(",")])
  buffer = f.readline()
  
buffer = f.readline()
parameters = buffer.strip().split()[2].split("=")
if parameters[0] == "x":
  for x in dots:
    if x[0] > int(parameters[1]):
      x[0] = 2 * int(parameters[1]) - x[0]
if parameters[0] == "y":
  for x in dots:
    if x[1] > int(parameters[1]):
      x[1] = 2 * int(parameters[1]) - x[1]
f.close()

set = []
for x in dots:
  if x not in set:
    set.append(x)
print(len(set))