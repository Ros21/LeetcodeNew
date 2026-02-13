"""
75. Sort Colors
"""
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
 
        # return nums



assert Solution().sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
assert Solution().sortColors([2,0,1]) == [0,1,2]
assert Solution().sortColors([0]) == [0]
assert Solution().sortColors([1]) == [1]    
assert Solution().sortColors([1,2,0]) == [0,1,2]
assert Solution().sortColors([2,1,0]) == [0,1,2]
assert Solution().sortColors([0,2,1]) == [0,1,2]
assert Solution().sortColors([1,0,2]) == [0,1,2]
