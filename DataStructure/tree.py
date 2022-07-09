
# class TreeNode:

#     def __init__(self, data, children=[]):
#         self.data = data
#         self.children = children

#     def __str__(self, level=0):
#         ret = "  " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level + 1)
#         return ret

#     def addChild(self, TreeNode):
#         self.children.append(TreeNode)


# tr = TreeNode("Drinks",[])
# hot = TreeNode("Hot",[])
# cold = TreeNode("Cold",[])
# tr.addChild(hot)
# tr.addChild(cold)
# tea = TreeNode("tea",[])
# coffee = TreeNode("coffee",[])
# hot.addChild(tea)
# hot.addChild(coffee)
# cola = TreeNode("cola",[])
# fanta = TreeNode("fanta",[])
# cold.addChild(cola)
# cold.addChild(fanta)

# print(tr)

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


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


tn = TreeNode("Drinks")
leftC = TreeNode("Hot")
rightC = TreeNode("Cold")
tn.leftChild = leftC
tn.rightChild = rightC
tea = TreeNode("tea")
coffee = TreeNode("coffee")
leftC.leftChild = tea
leftC.rightChild = coffee


def preOrderTravesal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTravesal(rootNode.leftChild)
    preOrderTravesal(rootNode.rightChild)


def inOrderTravesal(rootNode):
    if not rootNode:
        return
    inOrderTravesal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTravesal(rootNode.rightChild)


def postOrderTravesal(rootNode):
    if not rootNode:
        return
    postOrderTravesal(rootNode.leftChild)
    postOrderTravesal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTravesal(rootNode):
    if not rootNode:
        return
    else:
        customQu = Queue()
        customQu.enqueue(rootNode)
        while not(customQu.isEmpty()):
            root = customQu.dequeue()
            print(root.data)
            if root.leftChild:
                customQu.enqueue(root.leftChild)
            if root.rightChild:
                customQu.enqueue(root.rightChild)


# preOrderTravesal(tn)

# inOrderTravesal(tn)

# postOrderTravesal(tn)

# levelOrderTravesal(tn)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQu = Queue()
        customQu.enqueue(rootNode)
        while not(customQu.isEmpty()):
            root = customQu.dequeue()
            if root.data.lower() == nodeValue.lower():
                return "Suceess"
            if root.leftChild:
                customQu.enqueue(root.leftChild)
            if root.rightChild:
                customQu.enqueue(root.rightChild)
        return "Failure"

# print(searchBT(tn, "Tea"))


def insertNodeBT(rootNode, newNode):
    if not rootNode:
        return
    else:
        customQu = Queue()
        customQu.enqueue(rootNode)

        while not(customQu.isEmpty()):

            root = customQu.dequeue()

            if root.leftChild:
                customQu.enqueue(root.leftChild)
            else:
                root.leftChild = newNode
                return "Success"

            if root.rightChild:
                customQu.enqueue(root.rightChild)
            else:
                root.rightChild = newNode
                return "Success"

        return "Failure"


def insertBT(rootNode,newNode):
    if rootNode:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.leftChild:
                customQueue.enqueue(root.leftChild)
            else:
                root.leftChild = newNode
                return 

            if root.rightChild:
                customQueue.enqueue(root.rightChild)
            else:
                root.rightChild = newNode
                return
    else:
        return


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        cQ = Queue()
        cQ.enqueue(rootNode)
        while not(cQ.isEmpty()):
            root = cQ.dequeue()

            if root.leftChild:
                cQ.enqueue(root.leftChild)
            if root.rightChild:
                cQ.enqueue(root.rightChild)
        return root

def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        cQ = Queue()
        cQ.enqueue(rootNode)
        while not(cQ.isEmpty()):
            root = cQ.dequeue()

            if root is dNode:
                root = None
                return
            
            if root.leftChild:
                if root.leftChild is dNode:
                    root.leftChild = None
                    return
                cQ.enqueue(root.leftChild)
            if root.rightChild:
                if root.rightChild is dNode:
                    root.rightChild = None
                    return
                cQ.enqueue(root.rightChild)


def deleteNodeBT(rootNode, dNode):
    if not rootNode:
        return
    else:
        cQ = Queue()
        cQ.enqueue(rootNode)
        while not(cQ.isEmpty()):
            root = cQ.dequeue()

            if root.data == dNode:
                node = getDeepestNode(rootNode)
                root.data = node.data
                deleteDeepestNode(rootNode,node)
                return "Success"
            
            if root.leftChild:
                cQ.enqueue(root.leftChild)
            if root.rightChild:
                cQ.enqueue(root.rightChild)
        return "Failure"


# newNode = TreeNode("Cola")
# print(insertBT(tn, newNode))
# levelOrderTravesal(tn)



deleteNodeBT(tn,'Hot')
levelOrderTravesal(tn)
