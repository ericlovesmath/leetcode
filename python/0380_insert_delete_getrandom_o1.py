import random


class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        self.arr[idx] = self.arr[-1]
        self.map[self.arr[-1]] = idx
        del self.map[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
