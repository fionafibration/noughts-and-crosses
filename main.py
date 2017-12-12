from random import choice
from collections import Counter
import pprint
import sys
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
        return {"score": 0}

    moves = []
    for i in range(len(available)):
        move = {}
        move["index"] = available[i]

        boardstate[available[i]] = player;

    
        if (player == aiplayer):
            result = MiniMax(boardstate, humanplayer)
            move["score"] = result["score"]
        else:
            result = MiniMax(boardstate, aiplayer)
            move["score"] = result["score"]

        boardstate[available[i]] = 0

        moves.append(move)
    
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
    global board, humanplayer, aiplayer, piecemap
    
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
            print("Invalid move. What about noughts and crosses \ndon't you understand?")

    board[move] = humanplayer
    
    if winning(board, humanplayer):
        print("There has been an error in my programming.\nThis message should never be shown, because I always win.")
        input()
        return 1
    drawBoard(board, piecemap)

    print("Computer's move:")
    
    aimove = {}
    minmaxboard = deepcopy(board)
    
    aimove = MiniMax(minmaxboard, aiplayer)
    
    try:
        if aimove["index"] in countAvailablePositions(board):
            board[aimove["index"]] = aiplayer
            drawBoard(board, piecemap)
    except:
        if winning(board, aiplayer):
            drawBoard(board, piecemap)
            print("I won! I beat your sorry little ass!")
            input()
            return 1
        elif winning(board, humanplayer):
            print("There has been an error in my programming.\nThis message should never be shown, because I always win.")
            input()
            return 1
        elif len(countAvailablePositions(board)) == 0:
            print("Tie game! I'll get you next time!")
            input()
            return 1
        else:
            print("Fatal error!")
            input()
            return 1

if __name__ == "__main__":
        while True:
                print("STARTING GAME!!!!")
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
                        print("Not a valid option... Try again... idiot.")
                board = [0,0,0,
                         0,0,0,
                         0,0,0]
                while True:
                        if main():
                            break
