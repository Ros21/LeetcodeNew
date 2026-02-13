"""
905. Sort Array By Parity
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
            else:
                i+=1
        print(nums)
        return nums


assert Solution().sortArrayByParity([3,1,2,4]) == [4,2,1,3]
assert Solution().sortArrayByParity([0]) == [0]
assert Solution().sortArrayByParity([4,2,4,3,5,1]) == [4,2,4,5,1,3]
assert Solution().sortArrayByParity([1,3,5,7]) == [1,3,5,7]
