# creating a node
class Node:  
    def __init__(self, data):
        self.data = data
        self.ref = None

# creating a linked list
class Linked_List:

    # head initialize
    def __init__(self):
        self.head = None

    # add at the begining of LL
    def add_begin(self, data):
        new_node = Node(data) #10, 20
        new_node.ref = self.head #none, as12121
        self.head = new_node  #10
    
    # add at the last of LL
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # print every node of LL
    def print__LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.ref

# N1 = Node(3)
# print(N1)
LL1 = Linked_List()
LL1.add_end(2500)
LL1.add_begin(10)
LL1.add_end(1000)
LL1.add_begin(20)
LL1.add_end(2000)
LL1.print__LL()

