# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(self.value)
        if self.root is None:
            self.root = new_node
        temp = self.root
        temp.next = new_node

        return new_node.value


ll = LinkedList()
ll.insert(5)
ll.insert(6)
