import sys


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adj = []
        self.minDist = sys.maxsize


class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


class BellmanFord(object):
    hasCycle = False

    def calcShortestPath(self, vertexList, edgeList, startVertex):
        startVertex.minDist = 0
        for i in range(0, len(vertexList)-1):
            for edge in edgeList:
                u = edge.startVertex
                v = edge.targetVertex
                newDist = u.minDist + edge.weight
                if newDist < v.minDist:
                    v.minDist = newDist
                    v.predecessor = u
        for edge in edgeList:
            u = edge.startVertex
            v = edge.targetVertex
            newDist = u.minDist + edge.weight
            if newDist < v.minDist:
                hasCycle = True

    def getShortestPath(self, target):
        if not self.hasCycle:
            print("Shortestpath " + target.minDist)

            node = target
            while node is not None:
                print(Node)
                node = node.predecessor
        else:
            print("negetive Cycle Detected")
