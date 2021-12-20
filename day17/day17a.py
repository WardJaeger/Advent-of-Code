f = open("input.txt")
buffer = f.readline().strip()
f.close()

xRange = [int(x) for x in buffer.split()[2].strip("x=,").split("..")]
yRange = [int(y) for y in buffer.split()[3].strip("y=").split("..")]

yVel = abs(yRange[0])-1

print((yVel*(yVel+1))//2)