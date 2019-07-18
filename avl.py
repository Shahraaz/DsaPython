class Node(object):
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None


class Avl(object):

    def __init__(self):
        self.root = None

    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.left) - self.calcHeight(node.right)
        # if return > 1 left heavy
        # if return < -1 right heavy

    def rightRotate(self, node):
        if not node:
            return
        tempLeftChild = node.left
        t = tempLeftChild.right
        node.left = t
        tempLeftChild.right = node
        node.height = 1+max(self.calcHeight(node.left),
                            self.calcHeight(node.right))
        tempLeftChild.height = 1+max(self.calcHeight(tempLeftChild.left),
                                     self.calcHeight(tempLeftChild.right))
        return tempLeftChild

    def leftRotate(self, node):
        if not node:
            return
        temprightChild = node.right
        t = temprightChild.left
        node.right = t
        temprightChild.left = node
        node.height = 1+max(self.calcHeight(node.left),
                            self.calcHeight(node.right))
        temprightChild.height = 1+max(self.calcHeight(temprightChild.left),
                                      self.calcHeight(temprightChild.right))
        return temprightChild

    def insertNode(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self.insertNode(data, node.left)
        if data > node.data:
            node.right = self.insertNode(data, node.right)
        node.height = 1+max(self.calcHeight(node.left),
                            self.calcHeight(node.right))
        return self.settleViolation(data, node)

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def settleViolation(self, data, node):
        balance = self.calcBalance(node)
        # case left left Heavy
        if balance > 1 and data < node.left.data:
            return self.rightRotate(node)
        # case right right Heavy
        if balance < -1 and data > node.right.data:
            return self.leftRotate(node)
        # case left right Heavy
        if balance > 1 and data > node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        # case right left Heavy
        if balance < -1 and data < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

    def traverseInorder(self, node):
        if node.left:
            self.traverseInorder(node.left)
        print(node.data)
        if node.right:
            self.traverseInorder(node.right)

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)
        else:
            print("Empty Tree\n")

    def printHt(self):
        if self.root:
            print(self.root.height)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def predecessor(self, node):
        if not node.right:
            return node
        return self.predecessor(node.right)

    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left = self.removeNode(data, node.left)
        elif data > node.data:
            node.right = self.removeNode(data, node.right)
        else:
            if not node.left and not node.right:
                del node
                return None
            if not node.left:
                tempNode = node.right
                del node
                return tempNode
            if not node.right:
                tempNode = node.left
                del node
                return tempNode
            tempNode = self.predecessor(node.left)
            node.data = tempNode.data
            node.left = self.removeNode(tempNode.data, node.left)
        if not node:
            return node
        node.height = 1+max(self.calcHeight(node.left),
                            self.calcHeight(node.right))
        balance = self.calcBalance(node)
        # double left heavy Case
        if balance > 1 and self.calcBalance(node.left) >= 0:
            return self.rightRotate(node)
        # left right case
        if balance > 1 and self.calcBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        # right right case
        if balance < -1 and self.calcBalance(node.right) <= 0:
            return self.leftRotate(node)
        # right left case
        if balance < -1 and self.calcBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node


Tree = Avl()
# for i in range(1, 100000):
# Tree.insert(i)
# Tree.printHt()
# this prints 16
for i in range(1, 20000):
    Tree.insert(i)
# Tree.traverse()
Tree.printHt()
for i in range(1, 10000):
    Tree.remove(i)
    # print("Tree")
# Tree.traverse()
Tree.printHt()
