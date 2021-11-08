
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, value):
        self.items.append(value)
        return True

    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            return self.items.pop(0)


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Success"


'''
--- Traversal ---
Depth First Search (DFS)
    Pre Order Traversal  (Root-Left-Right)
    In Order Traversal   (Left-Root-Right)
    Post Order Traversal (Left-Right-Root)
Breadth First Search (BFS)
    Level Order Travesal
'''


def preOrderTravesal(rootNode):
    if rootNode:
        print(rootNode.data)
        preOrderTravesal(rootNode.leftChild)
        preOrderTravesal(rootNode.rightChild)
    else:
        return


def inOrderTravesal(rootNode):
    if rootNode:
        inOrderTravesal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTravesal(rootNode.rightChild)
    else:
        return


def postOrderTravesal(rootNode):
    if rootNode:
        postOrderTravesal(rootNode.leftChild)
        postOrderTravesal(rootNode.rightChild)
        print(rootNode.data)
    else:
        return


def levelOrderTravesal(rootNode):
    if rootNode:
        neQ = Queue()
        neQ.enqueue(rootNode)
        while not(neQ.isEmpty()):
            root = neQ.dequeue()
            print(root.data)
            if root.leftChild:
                neQ.enqueue(root.leftChild)
            if root.rightChild:
                neQ.enqueue(root.rightChild)
    else:
        return


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("Success")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("Success")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("Success") 
        else:
            searchNode(rootNode.rightChild, nodeValue)


newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)

# preOrderTravesal(newBST)
# inOrderTravesal(newBST)
# postOrderTravesal(newBST)
# levelOrderTravesal(newBST)


print(searchNode(newBST, 60))
print(searchNode(newBST, 62))
