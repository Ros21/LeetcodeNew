"""
3364. Minimum Positive Sum Subarray 
"""
class Solution:
    def minimumSumSubarray(self, nums, l: int, r: int) -> int:
        result = 0
        left=0
        sub_sum = sum(nums[:l])
        for right in range(l,len(nums)):
            pass
        return result


assert Solution().minimumSumSubarray([3, -2, 1, 4], 2, 3) == 1
# assert Solution().minimumSumSubarray([1,-2,3,4,5], 2, 3) == 4
# assert Solution().minimumSumSubarray([-1,-2,-3], 1, 2) == 0
# assert Solution().minimumSumSubarray([2,3,-1,4,-2,1], 3, 4) == 2
