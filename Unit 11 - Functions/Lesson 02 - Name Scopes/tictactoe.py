def drawBoard():
    for row in board:
        print(row)
    print()

def playerOneTurn():
    while(True):
        row = int(input("Enter row number: "))
        col = int(input("Enter col number: "))
        if board[row][col] == "-":
            board[row][col] = "X"
            break
        elif row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid entry try again")
        else:
            print("Invalid entry try again")

def playerTwoTurn():
    row = int(input("Enter row number: "))
    col = int(input("Enter col number: "))
    if board[row][col] == "-":
        board[row][col] = "O"
    elif row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid entry try again")
    else:
        print("Invalid entry try again")

def checkRowsForWin():
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return True
    return False

def checkColsForWin():
    if board[0][0] == board[1][0] == board[2][0] != "-":
        return True
    elif board[0][1] == board[1][1] == board[2][1] != "-":
        return True
    elif board[0][2] == board[1][2] == board[2][2] != "-":
        return True
    return False 

def checkLeftDiagonalForWin():
    return board[0][0] == board[1][1] == board[2][2] != "-"

def checkRightDiagonalForWin():
    return board[0][2] == board[1][1] == board[2][0] != "-"

def checkWin():
    rowWon = checkRowsForWin()
    colWon = checkColsForWin()
    leftWon = checkLeftDiagonalForWin()
    rightWon = checkRightDiagonalForWin()
    return rowWon or colWon or leftWon or rightWon

def gameloop():
    while (True):
        drawBoard()
        playerOneTurn()
        drawBoard()
        if (checkWin()):
            print("X Wins")
            break
        playerTwoTurn()
        drawBoard()
        if (checkWin()):
            print("O Wins")
            break

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

gameloop()
