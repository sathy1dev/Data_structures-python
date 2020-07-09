class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_before(self,new_data):

        new_node = node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self,new_data):

        new_node = node(new_data)

        if self.head is None: 
            self.head = new_node 
            return
        
        last = self.head
        while(last.next):
            last = last.next
    
    def printing(self):
        head = self.head
        while(head):
            print(head.data)
            head  = head.next

class problem:
    def loop(self,n):
        c = linkedlist()
        while(n):
            length_of_node = int(input('Enter the lenght of the node'))
            for i in range(length_of_node):
                node = int(input('Enter the node'))
                destination = int(input('Enter the node destination'))
               
                if destination == 0:
                    
                    c.insert_before(node)
                elif destination == 1:
                      c.insert_after(node)
                else:
                    print('Check your entry')     
            n -= 1
        c.printing()


total_number_of_cases = 1
g = problem()
g.loop(total_number_of_cases)
