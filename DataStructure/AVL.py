
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


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


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
    if not rootNode:
        return
    neQ = Queue()
    neQ.enqueue(rootNode)
    while not(neQ.isEmpty()):
        root = neQ.dequeue()
        print(root.data)
        if root.leftChild:
            neQ.enqueue(root.leftChild)
        if root.rightChild:
            neQ.enqueue(root.rightChild)

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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)

    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)

    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


nAVL = AVLNode(5)
nAVL = insertNode(nAVL, 10)
nAVL = insertNode(nAVL, 15)
nAVL = insertNode(nAVL, 20)
preOrderTravesal(nAVL)
