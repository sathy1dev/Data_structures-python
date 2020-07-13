class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    #inserting nodes at the begining of the linked list
    def push(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    #printing the linked list
    def printing(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    #deleting a node using a key value in a linked list
    def delete(self,key):
        #selecting the head node
        temp = self.head

        #checking if head node itself containts the contains the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        #search for the key while travelling in linked list and also keeping track of the previous node
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        #if the key was not present in linked list
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None

#declaring linkedlist class object
l_list = linkedlist()

#creating three nodes
l_list.push(1)
l_list.push(2)
l_list.push(3)

#deleting a specific node in a linked list
l_list.delete(2)

#printing our linked list
l_list.printing()