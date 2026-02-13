"""
128. Longest Consecutive Sequence
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        set --> 
        """
        nums_set = set(nums)
        length = 1
        max_length = 0
        for num in nums_set:
            if num-1 not in nums_set:
                length=1
                element = num+1
                while element in nums_set:
                    length+=1
                    element+=1
                max_length=max(length, max_length)
        return max_length


assert Solution().longestConsecutive([100,4,200,1,3,2]) == 4
assert Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
assert Solution().longestConsecutive([]) == 0
assert Solution().longestConsecutive([1,2,0,1]) == 3
assert Solution().longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]) == 7
assert Solution().longestConsecutive([1,3,5,2,4]) == 5
assert Solution().longestConsecutive([10,5,12,3,55,30,4,11,2]) == 4
assert Solution().longestConsecutive([1]) == 1
assert Solution().longestConsecutive([1,2]) == 2
assert Solution().longestConsecutive([2,1]) == 2