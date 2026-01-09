class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    #insertion
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data: #15 > 12
            if self.lchild:  #if exist true
                self.lchild.insert(data)  #call once again to compare
            else:
                self.lchild = BST(data) 
        else:
            if self.rchild:  #if exist true
                self.rchild.insert(data)  #call once again to compare
            else:
                self.rchild = BST(data)     
    #searching
    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the tree!")           

    # Pre-order traversal
    def preOrder(self):
        print(self.key, end = " ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    # In-order traversal
    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key, end = " ")
        if self.rchild:
            self.rchild.inOrder()

    # Post-order traversal
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key, end = " ")


root = BST(None)
list1 = [1,2,5,1,2,10,20,8]
for i in list1:
    root.insert(i)
root.search(1)
print("Pre-order")
root.preOrder()
print()
print("In-order")
root.inOrder()
print()
print("Post-order")
root.postOrder()
# print(root.rchild)
# print(root.lchild.key, root.lchild.lchild, root.lchild.rchild)
# print(root.rchild.key, root.rchild.lchild, root.rchild.rchild)
# print(root.rchild.rchild.key, root.rchild.rchild.lchild, root.rchild.rchild.rchild)