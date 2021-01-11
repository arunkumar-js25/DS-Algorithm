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
print(optimal_stategy(golds,0,len(golds)-1))
