"""
3289. The Two Sneaky Numbers of Digitville
"""
from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_count = {}
        result = set()
        for num in nums:
            if num in num_count:
                result.add(num)
            else:
                num_count[num] = num_count.get(num, 0) +1
        return list(result)


assert Solution().getSneakyNumbers([0,1,1,0]) == [0, 1]
assert Solution().getSneakyNumbers([0,3,2,1,3,2]) == [2, 3]
assert Solution().getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]) == [4, 5]

