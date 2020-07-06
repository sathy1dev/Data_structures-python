#we need to have two classes , node --> class and linked list --> class
#node class contains data and next(link to next node) and linkedlist class contains head node

#node class that contains data and next
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


#creating a linkedlist class with head node
class Linked_list:
    def __init__(self):
        self.head = None
    
    #function to print our linked list
    def printList(self):
        #getting the head node first
        head = self.head
        #looping through all the iterations of list
        while(head):
            #printing the head node data
            print(head.data)
            
            #accessing the second node
            head = head.next




#driver code
#declaring linked list to a variable "l_list"
l_list = Linked_list()

#creating a head node, with value (data) --> 1
l_list.head = Node(1)

#creating other 2 nodes, 
second = Node(2)
third = Node(3)

#linking all nodes together
l_list.head.next = second; #linking first node to the second
second.next = third

#printing our data in the linked list
l_list.printList()