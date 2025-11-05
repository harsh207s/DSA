import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.idx = {}   # val -> set of indices

    def insert(self, val: int) -> bool:
        exists = val in self.idx
        
        # add index in hashmap
        if not exists:
            self.idx[val] = set()
        
        self.idx[val].add(len(self.nums))
        self.nums.append(val)
        
        return not exists

    def remove(self, val: int) -> bool:
        if val not in self.idx or not self.idx[val]:
            return False
        
        # Remove one index of val
        remove_idx = self.idx[val].pop()
        last_val = self.nums[-1]

        # If removing not the last element, swap
        if remove_idx != len(self.nums) - 1:
            # Move last element into removed position
            self.nums[remove_idx] = last_val
            
            # Update the index set of the last value
            self.idx[last_val].remove(len(self.nums) - 1)
            self.idx[last_val].add(remove_idx)

        # finally remove last element
        self.nums.pop()

        # if no occurrences left, delete key
        if not self.idx[val]:
            del self.idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
