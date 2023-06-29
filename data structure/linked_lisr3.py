class Node:    
	def __init__(self,value):        
		self.value = value        
		self.next = None
		
'''
We add the value because for anything to be added to the linked list,
it should at least have some value
The next means that it is possible we want to chain other nodes – I mean, 
that is the major aim of a linked list.

'''
class LinkedList:
        def __init__(self,head=None):
                self.head = head 
       
        def append(self, new_node):
                current = self.head
                if current:
                    while current.next:
                        current = current.next
                    current.next = new_node
                else:
                    self.head = new_node

        def delete(self, value):
               """Delete the first node with a given value."""
               current = self.head
                        
               if current.value == value:
                    self.head = current.next
               else:
                    while current:
                        if current.value == value:
                            break
                        prev = current
                        current = current.next
                    if current == None:
                        return
                    prev.next = current.next
                    current = None
        def insert(self, new_element, position):
            '''Insert a new node at the given position.
            Assume the first position is "1".
            Inserting at position 3 means between
            the 2nd and 3rd elements.  '''
              
            count=1
            current = self.head
            if position == 1:
                new_element.next = self.head
                self.head = new_element
            while current:
                if count+1 == position:
                    new_element.next =current.next
                    current.next = new_element
                    return
                else:
                    count+=1
                    current = current.next
                # break
        def print(self):
             
            current = self.head
            while current:
                print(current.value)
                current = current.next


   


e1 = Node(1)
e2 = Node(2)
ll = LinkedList(e1)
l2= LinkedList(e2)
