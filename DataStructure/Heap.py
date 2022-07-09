class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekofHeap(rootNode):
    if rootNode:
        return rootNode.customList[1]
    return

def sizeofHeap(rootNode):
    if rootNode:
        return rootNode.heapSize
    return

def levelOrderTravesal(rootNode):
    if rootNode:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])
    return

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = index//2
    if index <= 1:
        return
    if heapType == "min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
    else:
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode,nodeValue,heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "is full"
    rootNode.heapSize += 1
    rootNode.customList[rootNode.heapSize] = nodeValue
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "Success"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex =  index * 2
    rightIndex =  index * 2 + 1
    swapChild = 0
    

hp = Heap(5)
insertNode(hp,4,"max")
insertNode(hp,5,"max")
insertNode(hp,2,"max")
insertNode(hp,1,"max")
levelOrderTravesal(hp)