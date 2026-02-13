"""
303. Range Sum Query - Immutable
"""
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1]+n)
        print(self.prefix)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]


        


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(2,4)
print(param_1)