class Node(object):
    def __init__(self, character):
        self.character = character
        self.left = None
        self.midlle = None
        self.right = None
        self.value = 0


class TST(object):
    def __init__(self):
        self.rootNode = None

    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)

    def putItem(self, node, key, value, index):
        c = key[index]
        if node == None:
            node = Node(c)
        if c < node.character:
            node.left = self.putItem(node.left, key, value, index)
        elif c > node.character:
            node.right = self.putItem(node.right, key, value, index)
        elif index < len(key) - 1:
            node.midlle = self.putItem(node.midlle, key, value, index+1)
        else:
            node.value = value
        return node

    def get(self, key):
        node = self.getItem(self.rootNode, key, 0)
        if node == None:
            return -1
        return node.value

    def getItem(self, node, key, index):
        if node == None:
            return None
        c = key[index]
        if c < node.character:
            return self.getItem(node.left, key, index)
        elif c > node.character:
            return self.getItem(node.right, key, index)
        elif index < len(key) - 1:
            return self.getItem(node.midlle, key, index+1)
        else:
            return node


tst = TST()
tst.put("apple", 100)
tst.put("orange", 200)
print(tst.get("apple"))
print(tst.get("orange"))
print(tst.get("ab"))
