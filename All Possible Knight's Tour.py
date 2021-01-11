#Print all Possible Knight’s Tours in a chessboard
#Given a chess board, print all sequences of moves of a knight on a chessboard such that the knight visits every square only once.

row = [2,1,-1,-2,-2,-1,1,2,2]
col = [1,2,2,1,-1,-2,-2,-1,1]

def isvalid(x,y):
    return not(x<0 or y<0 or x>=N or y>=N)   # y>=M different board size

def KnightTour(board,x,y,pos):
    board[x][y] = pos

    if pos >= N*N:                          # N*M
        for i in board:
            print(i)
        print()
        board[x][y] = 0 #BACKTRACKING

    for k in range(8): #POSSIBLE 8 STEPS for Knight in ChessBoard
        dx = x+row[k]
        dy = y+col[k]
        if isvalid(dx,dy) and board[dx][dy] ==0:
            KnightTour(board,dx,dy,pos+1)

    board[x][y] = 0

N=5
#M=4
board = [[0 for y in range(N)]for x in range(N)]  #Diff Board Size NxN , NxM
KnightTour(board,0,0,1)
