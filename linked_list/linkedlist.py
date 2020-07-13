#node class
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

#linked list class
class linkedlist:
    def _init__(self):
        self.head = None

    #printing the linked list
    def printing(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next 
#accessing linkedlist
l_list = linkedlist()

#creating three empty nodes
l_list.head = node(1)
second = node(2)
third = node(3)

#linking the nodes together
l_list.head.next = second; second.next = third

#printing the linked list
l_list.printing()