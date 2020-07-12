class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def printing(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def insert_at_begining(self,new_data):
        new_node = node(new_data)

        new_node.next = self.head

        self.head = new_node

    def insert_at_specific(self, prev_node, new_data):

        #if the list is empty , if yes make it as head
        if prev_node is None:
            print("The previous node must be linked to the linked list")
            return
        
        new_node = node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node
    
    def end(self,new_data):
        new_node = node(new_data)

        last = self.head

        while(last.next):
            last = last.next
        
        last.next = new_node


l_list = linkedlist()
l_list.head = node(1)
second = node(2)
third = node(3)

#link each nodes together
l_list.head.next = second
second.next = third

#insert at the beginning
l_list.insert_at_begining(4)

#insert node after a speicific node
l_list.insert_at_specific(second,5)

#insert at the end of the linked list
l_list.end(6)


#PRINTING THE NODE
l_list.printing()