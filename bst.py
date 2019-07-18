class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class Bst(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    # O(log N) if the tree is balanced
    def insertNode(self, data, root):
        if data < root.data:
            if root.leftChild:
                self.insertNode(data, root.leftChild)
            else:
                root.leftChild = Node(data)
        else:
            if root.rightChild:
                self.insertNode(data, root.rightChild)
            else:
                root.rightChild = Node(data)

    def predeccor(self, root):
        if root.rightChild:
            return self.predeccor(root.rightChild)
        return root

    def removeNode(self, data, root):
        if not root:
            return root
        if data < root.data:
            root.leftChild = self.removeNode(data, root.leftChild)
        elif data > root.data:
            root.rightChild = self.removeNode(data, root.rightChild)
        else:
            if not root.leftChild and not root.rightChild:
                del root
                return None
            if not root.leftChild:
                tempNode = root.rightChild
                del root
                return tempNode
            if not root.rightChild:
                tempNode = root.leftChild
                del root
                return tempNode
            tempNode = self.predeccor(root.leftChild)
            root.data = tempNode.data
            root.leftChild = self.removeNode(tempNode.data, root.leftChild)
        return root

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, root):
        if root.leftChild:
            return self.getMin(root.leftChild)
        return root.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, root):
        if root.rightChild:
            return self.getMax(root.rightChild)
        return root.data

    def traverse(self):
        if(self.root):
            self.traverseInorder(self.root)

    def traverseInorder(self, node):
        if node.leftChild:
            self.traverseInorder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.traverseInorder(node.rightChild)


B = Bst()

B.insert(10)
B.insert(5)
B.insert(15)
B.insert(6)
# print(B.getMinValue())
# print(B.getMaxValue())
B.traverse()
print("Tree")
B.remove(5)
B.traverse()
print("Tree")
B.remove(10)
B.traverse()
