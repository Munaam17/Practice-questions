class MyHashSet:

    def __init__(self):
        self.dictionary = {}

    def add(self, key: int) -> None:
        self.dictionary[key] = None

    def remove(self, key: int) -> None:
        if key in self.dictionary:
            del self.dictionary[key]   

    def contains(self, key: int) -> bool:
        return key in self.dictionary
    
Ob = MyHashSet()
Ob.add(1)
Ob.add(2)
print(Ob.contains(1))
print(Ob.contains(3))
Ob.add(2)
print(Ob.contains(2))
Ob.remove(2)
print(Ob.contains(2))   

