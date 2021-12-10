f = open("input.txt")

numbers = f.readline().strip("\n").split(",")
numbers = [int(x) for x in numbers]
bufferLine = f.readline()

boards = []
while bufferLine != "":
  board = []
  for i in range(5): 
    row = f.readline().strip("\n").split(" ")
    row = [int(x) for x in row if x != ""]
    board.append(row)
  boards.append(board)
  bufferLine = f.readline()

f.close()

def checkForWin(board, row, col):
  for i in range(5):
    if board[row][i] != -1:
      break
    elif i == 4:
      return True
  for i in range(5):
    if board[i][col] != -1:
      return False
    elif i == 4:
      return True

def getScore(board, num):
  sum = 0
  for row in board:
    for val in row:
      if val != -1:
        sum += val
  return sum * num

for x in numbers:
  for board in boards:
    for i in range(5):
      for j in range(5):
        if board[i][j] == x:
          board[i][j] = -1
          if checkForWin(board, i, j):
            print(getScore(board, x))
            quit()