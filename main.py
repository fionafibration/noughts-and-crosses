from random import choice
from collections import Counter
import pprint
from copy import deepcopy

humanplayer = 1
aiplayer = 2

sampleboard = "| | | |\n| | | |\n| | | |"""


def winning(boardstate, player):
    if ((boardstate[0] == player and boardstate[1] == player and boardstate[2] == player) or (boardstate[3] == player and boardstate[4] == player and boardstate[5] == player) or (boardstate[6] == player and boardstate[7] == player and boardstate[8] == player) or (boardstate[0] == player and boardstate[3] == player and boardstate[6] == player) or (boardstate[1] == player and boardstate[4] == player and boardstate[7] == player) or (boardstate[2] == player and boardstate[5] == player and boardstate[8] == player) or (boardstate[0] == player and boardstate[4] == player and boardstate[8] == player) or (boardstate[2] == player and boardstate[4] == player and boardstate[6] == player)):
        return True
    return False


def MiniMax(boardstate, player):
    global aiplayer, humanplayer

    available = countAvailablePositions(boardstate)

    if winning(boardstate, aiplayer):
        return {"score": 10, "index": None}
    elif winning(boardstate, humanplayer):
        return {"score": -10, "index": None}
    elif not len(available):
        return {"score": 0, "index": None}

    moves = []
    for i in range(len(available)):
        newboard = boardstate
        newboard[available[i]] = player

        move = {}
        move["index"] = available[i]
        if (player == aiplayer):
            result = MiniMax(newboard, humanplayer)
            move["index"] = result["index"]
            move["score"] = result["score"]
        else:
            result = MiniMax(newboard, aiplayer)
            move["index"] = result["index"]
            move["score"] = result["score"]
        moves.append(move)

    pprint.pprint(moves)
    
    bestmove = None
    if (player == aiplayer):
        bestscore = -1000000000
        for i in range(len(moves)):
            if (moves[i]["score"] > bestscore):
                bestscore = moves[i]["score"]
                bestmove = i
    else:
        bestscore = 1000000000
        for i in range(len(moves)):
            if (moves[i]["score"] < bestscore):
                bestscore = moves[i]["score"]
                bestmove = i

    return moves[bestmove]
    

def countAvailablePositions(boardstate):
    emptyspots = []
    for i, spot in enumerate(boardstate):
        if spot == 0:
            emptyspots.append(i)
    return emptyspots



def drawBoard(board, piecemap):
    pieces = list(map((lambda x: piecemap[x]), board))
    print("|%s|%s|%s|\n|%s|%s|%s|\n|%s|%s|%s|" % (pieces[0], pieces[1], pieces[2], pieces[3], pieces[4], pieces[5], pieces[6], pieces[7], pieces[8]))
    
def main():
    global board, humanplayer, aiplayer
    good = False
    while not good:
        try:
            piece = input("What piece would you like to be? (X or O)\n").strip().lower()
            piecemap = ""
            if piece == "x":
                piecemap = " XO"
            elif piece == "o":
                piecemap = " OX"
            else:
                raise ValueError
            good = True
        except:
            print("Not a valid option... Try again")
    print("Your move:\n")
    drawBoard(board, piecemap)
    good = False
    while not good:
        try:
            move = int(input("Please enter a number (1-9)"))
            if (0 < move < 10):
                if move - 1 in countAvailablePositions(board):
                    good = True
                    move -= 1
                else:
                       raise ValueError
            else:
                raise ValueError
        except:
            print("Invalid move")

    board[move] = humanplayer
    
    if winning(board, humanplayer):
        print("There has been an error in my programming.\nThis message should never be shown, because I always win.")
        input()
        sys.exit()
    
    drawBoard(board, piecemap)
    
    
    aimove = {}
    minmaxboard = copy.deepcopy(board)
    
    aimove = MiniMax(minmaxboard, aiplayer)
    
    if aimove["index"] in countAvailablePositions(board):
        board[aimove["index"]] = aiplayer
    else:
        print("Fatal error!")
        input()
        sys.exit()
    if winning(board, aiplayer):
        print("I won! I beat your sorry little ass!")
        input()
        sys.exit()

if __name__ == "__main__":
    board = [0,0,0,
             0,0,0,
             0,0,0]
    while True:
        main()
