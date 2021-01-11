from _collections import deque

class Node:
    def __init__(self,x,y,dist=0,path=None):
        self.x = x
        self.y = y
        self.dist = dist
        self.path = path

    def __hash__(self):
        return hash((self.x,self.y,self.dist))

    def __eq__(self, other):
        return (self.x,self.y,self.dist) == (other.x,other.y,other.dist)

    def __str__(self):
        return str(self.x)+' '+str(self.y)

row = [2,1,-1,-2,-2,-1,1,2,2]
col = [1,2,2,1,-1,-2,-2,-1,1]

def isvalid(x,y):
    return not(x<0 or y<0 or x>=N or y>=N)

def shortestpath(src,dest):
    visited = set()
    q = deque()
    q.append(src)
    while q:
        node = q.popleft()
        if node.x == dest.x and node.y == dest.y:
            return node

        if node not in visited:
            visited.add(node)

        for k in range(8):
            dx = node.x + row[k]
            dy = node.y + col[k]
            if isvalid(dx,dy):
                q.append(Node(dx,dy,node.dist+1,node))
    return None

def printpath(node):
    if node:
        printpath(node.path)
        print(node)

N = 8
src = Node(7,0)
dest = Node(0,7)
result = shortestpath(src,dest)
print("Minimum number of steps required is", result.dist)
print("Complete Path : ")
printpath(result.path)
print(dest)
