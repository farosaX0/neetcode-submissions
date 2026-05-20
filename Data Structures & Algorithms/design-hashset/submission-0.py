class MyHashSet:

    def __init__(self):
        self.entries = []

    def add(self, key: int) -> None:
        #check if there is another value in the hashset
        if not self.contains(key):
            self.entries.append([key])

    def remove(self, key: int) -> None:
        for i in range(len(self.entries)):
            if self.entries[i][0] == key:
                del self.entries[i]
                return

    def contains(self, key: int) -> bool:
        for i in range(len(self.entries)):
            if self.entries[i][0] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)