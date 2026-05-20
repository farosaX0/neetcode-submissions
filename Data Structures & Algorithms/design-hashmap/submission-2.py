class MyHashMap:

    def __init__(self, initLen=100):
        self.entries = []
        self.entriesCount = 0
        self.initLen = initLen
    def put(self, key: int, value: int) -> None:
        if len(self.entries) == 0:
            self.entries.append([key, value])
        else:
            for i in range(len(self.entries)):
                if self.entries[i][0] == key:
                    self.entries[i][1] = value
                    return
            self.entries.append([key, value])

    def get(self, key: int) -> int:
        for i in range(len(self.entries)):
            if self.entries[i][0] == key:
                if self.entries[i][1] or self.entries[i][1] == 0:
                    return self.entries[i][1]
        return -1
    def remove(self, key: int) -> None:
        for i in range(len(self.entries)):
            if self.entries[i][0] == key:
                del self.entries[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)