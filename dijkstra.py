import sys
import heapq


class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adj = []
        self.minDist = sys.maxsize

    def __cmp__(self, otherVertex):
        return self.cmp(self.minDist, otherVertex.minDist)

    def __lt__(self, other):
        selfPriority = self.minDist
        otherPriority = other.minDist
        return selfPriority < otherPriority


class Algorithm(object):
    def calculateShortestPath(self, vertexList, startVertex):
        q = []
        startVertex.minDist = 0
        heapq.heappush(q, startVertex)

        while len(q) > 0:
            actualVertex = heapq.heappop(q)
            for edge in actualVertex.adj:
                u = edge.startVertex
                v = edge.targetVertex
                newDist = u.minDist + edge.weight
                if newDist < v.minDist:
                    v.predecessor = actualVertex
                    v.minDist = newDist
                    heapq.heappush(q, v)
    def getShoretest(self, target):

        node = target
        while node is not None:
            print(node.NameError)
            node = node.prepredecessord


