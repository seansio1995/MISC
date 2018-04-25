class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}


    def addNeighbor(self,nbr,weight):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id)+' connectedTo: ' + str([x.id for x in self.connectedTo])


    def getConnections(self):
        return self.connectedTo.keys()



    def getId(self):
        return self.id


    def getWeight(self,nbr):
        return self.connectedTo[nbr]



class Graph:
    def __init__(self):
        self.vertexList={}
        self.numVertices=0

    def addVertex(self,key):
        self.numVertices=self.numVertices+1
        newVertex=Vertex(key)
        self.vertexList[key]=newVertex
        return newVertex


    def getVertex(self,n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None


    def __contains__(self,n):
        return n in self.vertexList


    def addEdge(self,a,b,cost):
        if a not in self.vertexList:
            res=self.addVertex(a)
        if b not in self.vertexList:
            res=self.addVertex(b)

        self.vertexList[a].addNeighbor(self.vertexList[b],cost)



    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())
g=Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,2)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print("\n")

#print(g.vertexList[0].getWeight(1))
