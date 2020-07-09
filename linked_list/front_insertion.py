#inserting a node at very first of the list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def before_insertion_print(self):
        head = self.head
        while(head):
            print(head.data)
            head  = head.next

#driver code
llist = Linkedlist()

#creating three empty nodes
llist.head = node(1)
second = node(2)
third = node(3)

#linking all the nodes together
llist.head.next = second
second.next = third

#printing the linked list before insertion
print("Printing the linked list before insertion...... ")
llist.before_insertion_print()

llist.inser(9)
