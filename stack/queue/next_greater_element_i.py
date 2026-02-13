"""
496. Next Greater Element I
"""
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater={}
        stack = []
        for num in nums2:
            while stack and stack[-1]<num:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        for num in stack:
            next_greater[num]=-1
        return [next_greater[num] for num in nums1]


assert Solution().nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
assert Solution().nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]
assert Solution().nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]) == [7,7,7,7,7]
assert Solution().nextGreaterElement([2,1,3], [1,2,3]) == [3,2,-1]
assert Solution().nextGreaterElement([1,2,3], [3,2,1]) == [-1,-1,-1]
