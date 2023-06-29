# simple example
class Node:

    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return str(self.data)

node_1 = Node(1)
node_2 = Node(33)
node_3 = Node(55)
node_4 = Node(66)
#linked
node_1.next = node_2 # 1-->33
node_2.next = node_3 # 33-->55
node_3.next = node_4

lst = [node_1.data, node_1.next.data, (node_1.next).next.data ,(node_1.next).next.next.data]
print(lst)