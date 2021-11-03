'''
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return " ".join([ str(i) for i in self.items])

    def isEmpty(self):
        return self.items == []

    def enqueue(self,value):
        self.items.append(value)
        return True

    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[0]

    def delete(self):
        self.items = None

cq = Queue()

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)

print(cq)

'''
