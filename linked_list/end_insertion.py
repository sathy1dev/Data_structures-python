class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def printing(self):
        head = self.head
        #traversing or travelling through all the nodes in the linked list
        while(head):
            print(head.data)
            head = head.next
    
    def last_insertion(self,new_data):
        new_node = node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
        
        print("The last node is : ",last)

        last.next = new_node



llist = linkedlist()

#creating three empty nodes
llist.head = node(1)
second = node(2)
third = node(3)

#linking the nodes together
llist.head.next = second
second.next = third

llist.printing()
llist.last_insertion(7)
llist.printing()