'''
https://www.techiedelight.com/pots-gold-game-dynamic-programming/

PROBLEM:
In Pots of gold game, there are two players A & B and pots of gold arranged in a line, each containing some gold coins. 
The players can see how many coins are there in each gold pot and each player gets alternating turns in which the player can pick a pot from one of the ends of the line. 
The winner is the player which has a higher number of coins at the end. 
The objective is to “maximize” the number of coins collected by A, assuming B also plays optimally and A starts the game.
'''

Optimal Strategy:
#Get maximum no.of.gold from the line only by removing gold at end.. Guess optimal ways to get gold coins to win



def optimal_stategy(line,i,j):

    if(i==j):
        return line[i]
    elif(i+1 == j):
        return max(line[i],line[j])

    start = line[i] + min (optimal_stategy(line,i+2,j),optimal_stategy(line,i+1,j-1))
    end = line[j] + min(optimal_stategy(line,i+1,j-1),optimal_stategy(line,i,j-2))
    return max(start,end)


golds = [4,6,2,3]
print("Maximum coins collected by player is", optimal_stategy(golds,0,len(golds)-1))


#DYNAMIC PROGRAMMING -  to avoid running recursion over and over on computed strategy
def calculate(T, i, j):
    return T[i][j] if i <= j else 0
 

    
def optimalStrategy(coin):
    n = len(coin)
 
    if n == 1:
        return coin[0]
    if n == 2:
        return max(coin[0], coin[1])
 
    # create a dynamic 2D matrix to store sub-problem solutions
    T = [[0 for x in range(n)] for y in range(n)]
 
    for iteration in range(n):
        i = 0
        j = iteration
        while j < n:
            start = coin[i] + min(calculate(T, i + 2, j), calculate(T, i + 1, j - 1))
            end = coin[j] + min(calculate(T, i + 1, j - 1), calculate(T, i, j - 2))
            T[i][j] = max(start, end)
            i = i + 1
            j = j + 1
 
    return T[0][n - 1]
 
# pots of gold arranged in a line
coin = [4, 6, 2, 3]
print("Maximum coins collected by player is", optimalStrategy(coin))
