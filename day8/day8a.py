count = 0

f = open("input.txt")
buffer = f.readline()

while buffer != "":
  outputs = buffer.split("|")[1].strip().split()
  for x in outputs:
    if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7:
      count += 1
  buffer = f.readline()
  
f.close()

print(count)