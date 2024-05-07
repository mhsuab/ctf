# TicTacToe IA Never Lost
# https://github.com/lrmendes/TicTacToe-Never-Lose-AI

from typing import List, Tuple


GHOST = 'O'
PLAYER = 'X'
EMPTY = '-'

#  Rule 1: Check IF Machine or Player can Win [ IF needs 1 place to Win ]
def machineRule1(marker: str, board: List[ List[str] ]) -> Tuple[int, int]:
    markedD = 0
    markedID = 0
    checkD = []
    checkID = []
    cont = 0
    for i in range(len(board)):
        markedH = 0
        markedV = 0
        checkV = []
        checkH = []
        for a in range(len(board)):
            # Check Horizontal Win
            if (board[i][a] == marker):
                markedH += 1
            elif (board[i][a] == EMPTY):
                checkH = [i,a]

            # IF Horizontal Win -> Return
            if (markedH == 2 and checkH != []):
                return checkH;      

            # Check Vertical Win
            if (board[a][i] == marker):
                markedV += 1
            elif (board[a][i] == EMPTY):
                checkV = [a,i]  

            # IF Vertical Win -> Return
            if (markedV == 2 and checkV != []):
                return checkV;        
            
        # Check Diagonal Win
        if (board[i][i] == marker):
            markedD += 1
        elif (board[i][i] == EMPTY):
            checkD = [i,i]

        # IF Diagonal Win -> Return
        if (markedD == 2 and checkD != []):
            return checkD;   

        # Check Inverse Diagonal Win
        if (board[i][cont] == marker):
            markedID += 1
        elif (board[i][cont] == EMPTY):
            checkID = [i,cont]

        # IF Inverse Diagonal Win -> Return
        if (markedID == 2 and checkID != []):
            return checkID;   

        cont = cont - 1

    if (marker == PLAYER):
        return machineRule1(GHOST, board)
    else:
        return machineRule2(board)

# Rule 2: IF the center is open -> fill the center
def machineRule2(board):
    if (board[1][1] == EMPTY):
        return [1,1]
    else:
        return machineRule3(board)

# Rule 3: IF player fill a corner -> fill the opposite corner
def machineRule3(board):
    if(board[0][0] == GHOST and board[2][2] == EMPTY):
        return [2,2]
    if(board[0][0] == EMPTY and board[2][2] == GHOST):
        return [0,0]
    if(board[0][2] == GHOST and board[2][0] == EMPTY):
        return [2,0]
    if(board[2][0] == GHOST and board[0][2] == EMPTY):
        return [0,2]
    return machineRule4(board)

# Rule 4: If pla 
def machineRule4(board):
    if ( (board[0][0] == GHOST and board[2][2] == GHOST) or (board[0][2] == GHOST and board[2][0] == GHOST) ):
        if(board[0][1] == EMPTY):
            return [0,1]
        elif(board[1][0] == EMPTY):
            return [1,0]
        elif(board[1][2] == EMPTY):
            return [1][2]
        elif(board[2][1] == EMPTY):
            return [2][1]
    return machineRule5(board)

# Rule 5: If none of the previous rules were used, fill in any a corner. 
def machineRule5(board):
    if(board[0][0] == EMPTY):
        return [0,0]
    if(board[0][2] == EMPTY):
        return [0,2]
    if(board[2][0] == EMPTY):
        return [2,0]
    if(board[2][2] == EMPTY):
        return [2,2]
    return machineRule6(board)

# Rule 5: If none of the previous rules were used, fill the first availabe place. 
def machineRule6(board):
    for i in range(len(board)):
        for a in range(len(board)):
            if (board[i][a] == EMPTY):
                return [i,a]
    return False

