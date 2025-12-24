class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data) #10, 20
        new_node.ref = self.head #10-121sd,
        self.head = new_node  #10

    def print__LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

# N1 = Node(3)
# print(N1)
LL1 = Linked_List()
LL1.add_begin(10)
# LL1.add_begin()new_node.ref
LL1.add_begin(20)
LL1.print__LL()

