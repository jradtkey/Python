import sys

board = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

turn = ["Red"]

def show_board():
    for row in board:
        print row
    print (1,2,3,4,5,6)

def getMove():
    #ask user to choose which column to drop to the piece in
    makeMove = input(turn[0] + "'s turn. Pick a column: ")

    #if the user selects a column from outside the board, ask again
    while (makeMove < 1 or makeMove > 6):
        makeMove = input("Please choose a row from 1 to 6: ")

    #return -1 for accurate idx (first idx = 0 )
    return makeMove - 1

def place_piece(column):
    idx = -1
    for row in range(len(board)):
        if board[row][column] == 0:
            idx += 1
    board[idx][column] = turn[0]
    check_winner(idx, column)

def game_over():
    print turn[0], "player wins!"
    sys.exit(0)

def check_winner(idx, column):
    show_board()
    count = 0
    diagonal = 0

    print "ROW: ", idx
    print "COLUMN: ", column
    #check for horizontall win
    for i in range(len(board[idx])):
        if board[idx][i] == turn[0]:
            count += 1
            if count == 4:
                game_over()
        else:
            count = 0

    #check for vertical win
    for j in range(len(board)):
        if board[j][column] == turn[0]:
            count += 1
            if count == 4:
                game_over()
        else:
            count = 0

    #check for diagonal win
    for row in board:
        for value in range(len(board)):
            if row[value] == turn[0]:
                count += 1
    print "COUNT:", count            
    switch_player(turn[0])
    place_piece(getMove())



def switch_player(player):
    if player == "Red":
        turn[0] = "Blue"
    else:
        turn[0] = "Red"

# START GAME
show_board()
place_piece(getMove())
