"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4



[1,2,3,4]
1,2,3
1,2,4
1,3,4
2,3,4
"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        pass


print(Solution().triangleNumber([2,2,3,4]))  # Output: 3
print(Solution().triangleNumber([4,2,3,4]))  # Output: 4
print(Solution().triangleNumber([0,1,1,1]))  # Output: 0
print(Solution().triangleNumber([1,1,1,1]))  # Output: 4
print(Solution().triangleNumber([3,4,6,7]))  # Output: 3

