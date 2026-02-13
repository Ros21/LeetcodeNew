"""
27. Remove Element
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)
        while i<j:
            if nums[i]==val:
                nums[i]=nums[j-1]
                j-=1
            else:
                i+=1
        return j


assert Solution().removeElement([3,2,2,3], 3) == 2
assert Solution().removeElement([0,1,2,2,3,0,4,2], 2) == 5
assert Solution().removeElement([0,1,2,2,3,0,4,2], 0) == 6
assert Solution().removeElement([0], 0) == 0
assert Solution().removeElement([1], 0) == 1
assert Solution().removeElement([4,5], 4) == 1
assert Solution().removeElement([4,5], 6) == 2
assert Solution().removeElement([4,4,4,4], 4) == 0
assert Solution().removeElement([], 1) == 0