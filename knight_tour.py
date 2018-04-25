from enum import Enum

class State(Enum):
    unvisited = 1 #White
    visited = 2 #Black
    visiting = 3 #Gray


from collections import OrderedDict

class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node, val = weight

    def __str__(self):
        return str(self.num)


class Graph:

    def __init__(self):
        self.nodes = OrderedDict()  # key = node id, val = node

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight


def knightGraph(size):
    knightGraph=Graph()
    for row in range(size):
        for col in range(size):
            nodeID=posID(row,col,size)
            newPos=getLegalMove(row,col,size)
            for e in newPos:
                newNodeID=posID(e[0],e[1],size)
                knightGraph.add_edge(nodeID,newNodeID)
    return knightGraph



def posID(row,col,size):
    return row*size+col


def getLegalMove(row,col,size):
    newMoves=[]
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for offset in moveOffsets:
        newRow=row+offset[0]
        newCol=col+offset[1]
        if leglCoord(newRow,size) and legalCoord(newCol,size):
            newMoves.append((newRow,newCol))
    return newMoves



def legalCoord(x,size):
    if x>=0 and x<size:
        return True
    else:
        return False


def knightTour(n,path,u,limit):
    u.setColor("gray")
    path.append(u)
    if n < limit:
        nbrList=list(u.getConnections())
        i=0
        done=False
        while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else:
            done = True
        return done
