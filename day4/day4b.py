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

winningBoards = []

for x in numbers:
  for bI in range(len(boards)):
    if bI not in winningBoards:
      for i in range(5):
        for j in range(5):
          if boards[bI][i][j] == x:
            boards[bI][i][j] = -1
            if checkForWin(boards[bI], i, j):
              winningBoards.append(bI)
              if len(winningBoards) == len(boards):
                print(getScore(boards[bI], x))
                quit()