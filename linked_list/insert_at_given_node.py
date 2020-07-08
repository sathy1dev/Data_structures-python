class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def printing(self):
        head = self.head
        print("Printing the linked  list")
        while(head):
            print(head.data)
            head = head.next

    def insert_after(self,prev_node,new_data):
        print("\n Inserting a new node after 2")
        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node        
        
llist = linkedlist()

#creating three nodes
llist.head = node(1)
second = node(2)
third = node(3)

#linking the linked list
llist.head.next = second
second.next = third
llist.printing()
llist.insert_after(second,4)
llist.printing()