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
        if self.key == None:
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



root = BST(10)
# root.lchild = BST(5)
# root.rchild = BST(2)
# root.rchild.rchild = BST(3)
list1 = [1,2,5,1,2,10,20,8]
for i in list1:
    root.insert(i)
root.search(3)
print(root.rchild)
# print(root.lchild.key, root.lchild.lchild, root.lchild.rchild)
# print(root.rchild.key, root.rchild.lchild, root.rchild.rchild)
# print(root.rchild.rchild.key, root.rchild.rchild.lchild, root.rchild.rchild.rchild)