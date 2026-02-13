"""
3379. Transformed Array
"""
from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        for index in range(len(result)):
            if nums[index]==0: 
                result[index]= nums[index]
            else:
                final_index = (index+nums[index])%n
                result[index] = nums[final_index]
                
        return result


print(Solution().constructTransformedArray([3,-2,1,1]))  # [1,1,1,3]
print(Solution().constructTransformedArray([-1,4,-1]))  # [-1,-1,4]