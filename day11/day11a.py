f = open("input.txt")
energies = [[int(y) for y in x.strip()] for x in f.readlines()]
f.close()

flashes = 0

def flashIncrement(i, j):
  if i >= 0 and i < len(energies) and j >= 0 and j < len(energies[i]) and energies[i][j]:
    energies[i][j] += 1
    if energies[i][j] > 9:
      flash(i, j)

def flash(i, j):
  global flashes
  if energies[i][j] > 9:
    flashes += 1
    energies[i][j] = 0
    flashIncrement(i-1, j-1)
    flashIncrement(i-1, j)
    flashIncrement(i-1, j+1)
    flashIncrement(i, j+1)
    flashIncrement(i+1, j+1)
    flashIncrement(i+1, j)
    flashIncrement(i+1, j-1)
    flashIncrement(i, j-1)

for _ in range(100):
  for i in range(len(energies)):
    for j in range(len(energies[i])):
      energies[i][j] += 1
  for i in range(len(energies)):
    for j in range(len(energies[i])):
      flash(i, j)

print(flashes)