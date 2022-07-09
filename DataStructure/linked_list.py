
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseSLL(self):
        if self.head:
            node =  self.head
            while node:
                print(node.value)
                node = node.next
        else:
            print("List is empty")
    def traverseSLL(self):
        if self.head:
            node =  self.head
            while node:
                print(node.value)
                node = node.next
        else:
            print("List is empty")
    
    def searchSLL(self,value):
        if self.head:
            index = 0
            node =  self.head
            while node:
                if node.value == value:
                    return index
                node = node.next
                index += 1
        else:
            return -1
        

sing = SLinkedList()
sing.insertSLL(1,1)
sing.insertSLL(2,1)
sing.insertSLL(3,1)
sing.insertSLL(0,0)
sing.insertSLL(9,3)
print(sing.searchSLL(0))