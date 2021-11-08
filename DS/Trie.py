from types import coroutine


class TriNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfSting = False

class Trie:
    def __init__(self) -> None:
        self.root = TriNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if not node:
                node = TriNode()
                current.children.update({ch:node})
            current = node
        current.endOfSting = True

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if not node:
                return False
            currentNode = node
        return currentNode.endOfSting

def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word,index)
        return False

    if index == len(word) -1:
        if len(currentNode.children) >= 1:
            currentNode.endOfSting = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfSting == True:
        deleteString(currentNode,word,index+1)
        return False

    canThisNodeBeDeleted =  deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


nTrie = Trie()
nTrie.insertString("App")
nTrie.insertString("Appl")
deleteString(nTrie.root, "App", 0)
print(nTrie.searchString("App"))