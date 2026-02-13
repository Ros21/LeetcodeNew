"""
238. Product of Array Except Self
"""
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix*=nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]*= suffix
            suffix*=nums[i]
        return result


assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert Solution().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
assert Solution().productExceptSelf([0,0]) == [0,0]
