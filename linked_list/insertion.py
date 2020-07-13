class node:
    def __init__(self,data):
        self.data = data
        self.next = None

#linked list class
class linkedlist:

    def __init__(self):
        self.head = None
    
    #inserting a node at beginning of the linked list
    def push(self, new_data):
        #creating a new node based on data recieved
        new_node = node(new_data)        
        #making the next of new node as head
        new_node.next = self.head
        #move the head to the new node
        self.head = new_node
    
    #inserting a node at the end of the linked list

    def append(self,new_data):
        #creating a new node based on the new data
        new_node = node(new_data)
        #if the linked list is empty make the new node as head
        if self.head is None:
            self.head = new_node
            return
        #otherwise travelling through the list to find the last node
        last = self.head
        while(last.next):
            last = last.next
        #change the next of last node to new node
        last.next = new_node
    
    #inserting after a specific node
    def insert_after(self,prev_node,new_data):
        new_node = node(new_data)
        #telling that new_node next is equal to previous node next
        new_node.next = prev_node.next
        #telling that previous node next is the new node
        prev_node.next = new_node

    #printing the linked list
    def printing(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
if __name__=='__main__': 
#accessing linkedlist class
    l_list = linkedlist()

    #inserting a new node at the end
    l_list.append(7)
    l_list.append(9)

    #inserting at the beginning of the list
    l_list.push(8)
    l_list.push(6)
    l_list.push(5)
    l_list.push(4)

    #inserting after the first node
    l_list.insert_after(l_list.head,3)

    #printing the list
    l_list.printing()