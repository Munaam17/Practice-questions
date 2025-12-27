# creating a node
class Node:  
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self,data,x):
        # Adding after 
        if self.head is None:
            print("LL is empty!")
        else:
            n =self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self,data,x):
        # Adding before 
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref                
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
                                              
    # Traverse every node of D_LL forward
    def print__D_LL_F(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.nref

    # Traverse every node of D_LL reverse
    def print__D_LL_R(self):
        print()
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.pref


# Node(10)
DLL = Doubly_Linked_List()
DLL.insert_empty(30)
DLL.add_begin(10)
DLL.add_begin(20)
DLL.add_end(30)
DLL.add_after(21,220)
DLL.add_before(21,20)
DLL.add_before(21,20)
DLL.print__D_LL_F()
# DLL.print__D_LL_R()


