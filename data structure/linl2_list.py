class Node:
    def __init__(self, data = None):
        self. data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        current_node = self.head 
        new_node = Node(data) #creates new object

        #linked new node with the last node - go over the list
        while current_node.next != None:
             current_node = current_node.next #go to the last node
        current_node.next = new_node #the next one , after it, will recived the value which we will input

    def display(self):
        elems = []
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)
    
    def find_node(head, i):
        if head <=0:
            return None
        else:
            while head and i>0 :
                 i-=1
                 head=head.next()
                 return head

my_list = Linked_list()
my_list.display()

my_list.append(1)
my_list.append(1)
my_list.display()