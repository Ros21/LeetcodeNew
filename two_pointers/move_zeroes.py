"""
283. Move Zeroes
"""
import re


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right], nums[left]
                left+=1
        return nums


assert Solution().moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
assert Solution().moveZeroes([0]) == [0]
assert Solution().moveZeroes([4,2,4,0,0,3,5,1,0]) == [4,2,4,3,5,1,0,0,0]