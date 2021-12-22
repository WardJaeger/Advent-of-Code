f = open("input.txt")
enhance = [int(x=="#") for x in f.readline().strip()]
f.readline()
image = [[int(y=="#") for y in x.strip()] for x in f.readlines()]
f.close()

empty = 0
def doEnhance():
  global enhance, image, empty
  newImage = []
  size = len(image)
  for x in range(size+2):
    newImage.append([])
    for y in range(size+2):
      value = 0
      for i in range(-1,2):
        for j in range(-1,2):
          value *= 2
          if x+i < 1 or x+i > size or y+j < 1 or y+j > size:
            value += empty
          else:
            value += image[x+i-1][y+j-1]
      newImage[x].append(enhance[value])
  if empty:
    empty = enhance[len(enhance)-1]
  else:
    empty = enhance[0]
  image = newImage

for _ in range(50):
  doEnhance()

pixels = 0
for x in image:
  for y in x:
    pixels += y

print(pixels)