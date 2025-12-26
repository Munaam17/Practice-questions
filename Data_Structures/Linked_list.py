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
            while n.ref is not None: #self.head.ref
                n = n.ref   #n = self.head.ref 2100, ,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
            n.ref = new_node


    def add_after(self, data, x):

        # ADDING AFTER THE FIRST NODE
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):

        # ADDING BEFORE THE FIRST NODE
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            new_node = Node(data) #10, 20
            new_node.ref = self.head #none, as12121
            self.head = new_node  #10
            return
        
        # ADDING BEFORE ANY OTHER NODE IN LL
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

        # WHEN LL IS EMPTY
    def insert_Empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is not empty")

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
LL1.insert_Empty(35)
LL1.add_end(2500)
LL1.add_begin(10)
LL1.add_end(1000)
LL1.add_after(1080, 1000)
# LL1.add_begin(20)
# LL1.add_end(2000)
# LL1.add_before(500, 2500)
# LL1.add_after(35, 10)
LL1.print__LL()

