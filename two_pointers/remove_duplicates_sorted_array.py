"""
26. Remove Duplicates from Sorted Array
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        while right<len(nums):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left+=1
            right+=1
        return left
                


assert Solution().removeDuplicates([1,1,2]) == 2
assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
assert Solution().removeDuplicates([1,2,3,4,5]) == 5
assert Solution().removeDuplicates([1,1,1,1,1]) == 1
assert Solution().removeDuplicates([1]) == 1
assert Solution().removeDuplicates([1,1]) == 1
assert Solution().removeDuplicates([1,2]) == 2