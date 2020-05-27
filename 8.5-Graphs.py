#Implementing the graph ADT. There will be two classes, Vertex and graph

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, newN, weight = 0):
        self.connectedTo[newN] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, neigh):
        return self.connectedTo[neigh]

    def getId(self):
        return self.id

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def connectVertex(self, fromV, toV, w):
        if fromV not in self.vertList:
            addVertex(fromV)
        if toV not in self.vertList:
            addVertex(toV)
        self.vertList[fromV].addNeighbour(self.vertList[toV], weight = w)

    def getVertices:
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
