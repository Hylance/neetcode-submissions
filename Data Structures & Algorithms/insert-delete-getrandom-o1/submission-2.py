class RandomizedSet:

    def __init__(self):
        self.numSet = set()
        self.size = 0
        
    def insert(self, val: int) -> bool:
        if val in self.numSet:
            return False
        self.numSet.add(val)
        self.size += 1
        

    def remove(self, val: int) -> bool:
        if val not in self.numSet:
            return False
        self.numSet.remove(val)
        self.size -= 1
        return True
        

    def getRandom(self) -> int:
        idx = random.randrange(0, self.size)
        return list(self.numSet)[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()