def stringify(node):
    if not node:
        return 'None'
    return f"{str(node.data)} -> {stringify(node.next)}"


class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    

print(stringify(Node(0, Node(1, Node(2, Node(3))))))

"""
print(, '0 -> 1 -> 2 -> 3 -> None')
print(stringify(None), 'None')
print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))), '0 -> 1 -> 4 -> 9 -> 16 -> None')
"""