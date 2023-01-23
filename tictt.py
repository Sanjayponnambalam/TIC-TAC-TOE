import random


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
while True:
    a=input("DO YOU WANNA BE X OR O : ")
    if a not in "xXOo":
        print("\nIt's an Invalid Input\n\nPlease type either x or y\n")
        continue
    else:
        break

if ((a=="X")or(a=="x")):
   player = "X"
else:
   player = "O"
winner = None
game = True
print("YOUR BOARD FORMAT WITH POSITIONS : ")

print("1" +  " | " + "2" + " | " + "3" )
print("---------")
print("4" + " | "  + "5" + " | " + "6" )
print("---------")
print("7" + " | "  + "8" + " | " + "9" )
print()
# game board
def printBoard(board):
    print(board[0] +  " | " + board[1] + " | " + board[2] )
    print("---------")
    print(board[3] + " | "  + board[4] + " | " + board[5] )
    print("---------")
    print(board[6] + " | "  + board[7] + " | " + board[8] )


# take player input
def playerInput(board):
    while True:
         
        try:
           inp = int(input("Select a spot between 1 and 9: "))
           if (inp>9):
                print("INVALID INPUT!\n\nPlease Enter a value between 1 and 9")
                continue
           else:
                if board[inp-1] == "-":
                  board[inp-1] = player
                else:
                    if board[inp-1] in "Oo":
                        print("\nThe opposite player has taken that spot already.\n\nPlease try a different spot.")
                        continue
                    else :
                        print("\nThe position has already been chosen by you!\nPlease try a different spot.\n\n")
                        continue
           
            
        except ValueError:  
           print("INVALID INPUT!\n\nPlease Enter a value between 1 and 9\n")
        else:      
           break
    

# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global game
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        game = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        game = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        game = False
    

def checkIfTie(board):
    global game
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        game = False
    


# switch player
def switchPlayer():
    global player
    if (player=="X"):
       
       if player == "X":
          player = "O"
        
       else:
          player = "X"
    elif (player=="O"):
       if player == "O":
          player = "X"
        
       else:
          player = "O"


def computer(board):
    if (player=="O"):
      while player == "O":
           position = random.randint(0, 8)
           if board[position] == "-":
              board[position] = "O"
              switchPlayer()
    elif (player == "X"):
      while player == "X":
           position = random.randint(0, 8)
           if board[position] == "-":
              board[position] = "X"
              switchPlayer()


while game:
    
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
    
