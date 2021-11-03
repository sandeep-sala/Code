'''
class StackList:

    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        return str(self.list[::-1])

    def isEmpty(self):
        return self.list == []
    
    def push(self,ele):
        self.list.append(ele)
        return True

    def pop(self):
        if self.isEmpty():
            return False
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return []
        else:
            return self.list[-1]
    
    def delete(self):
        self.list = []

cs = StackList()
cs.push(1)
cs.push(2)
cs.push(3)
print(cs)
print(cs.pop())
print(cs)
print(cs.peek())
'''

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class StackLinkedList:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def __str__(self) -> str:
        value = [ str(i.value) for i in self.LinkedList]
        return "\n".join(value)

    def isEmpty(self):
        return self.LinkedList.head == None 

    def push(self,ele):
        node  = Node(ele)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        return True

    def pop(self):
        if self.isEmpty():
            return False
        else:
            nodeValue =  self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next 
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return []
        else:
            nodeValue =  self.LinkedList.head.value
            return nodeValue
    
    def delete(self):
        self.LinkedList.head = None
    


cs = StackLinkedList()
cs.push(1)
cs.push(2)
cs.push(3)
print(cs)
cs.pop()
print(cs)

print(cs.isEmpty())