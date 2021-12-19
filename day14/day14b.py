f = open("input.txt")
polymer = f.readline().strip()
f.readline()
rules = [[y.strip() for y in x.split("->")] for x in f.readlines()]
f.close()

def incDict(dictionary, key, amount):
  if key in dictionary:
    dictionary[key] += amount
  else:
    dictionary[key] = amount

pairs = {}
for i in range(len(polymer)-1):
  incDict(pairs, polymer[i:i+2], 1)

for _ in range(40):
  newPairs = {}
  for pair in pairs:
    flag = True
    for rule in rules:
      if rule[0] == pair:
        flag = False
        incDict(newPairs, pair[0] + rule[1], pairs[pair])
        incDict(newPairs, rule[1] + pair[1], pairs[pair])
        break
    if flag:
      incDict(newPairs, pair, pairs[pair])
  pairs = newPairs

characters = {}
for pair in pairs:
  incDict(characters, pair[0], pairs[pair])
incDict(characters, polymer[-1], 1)
print(max(characters.values()) - min(characters.values()))