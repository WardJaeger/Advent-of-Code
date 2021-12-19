f = open("input.txt")
polymer = f.readline().strip()
f.readline()
rules = [[y.strip() for y in x.split("->")] for x in f.readlines()]
f.close()

for _ in range(10):
  newPolymer = ""
  for i in range(len(polymer)-1):
    newPolymer += polymer[i]
    for x in rules:
      if x[0] == polymer[i:i+2]:
        newPolymer += x[1]
        break
  newPolymer += polymer[-1]
  polymer = newPolymer

characters = {}
for c in polymer:
  if c in characters:
    characters[c] += 1
  else:
    characters[c] = 1
print(max(characters.values())- min(characters.values()))