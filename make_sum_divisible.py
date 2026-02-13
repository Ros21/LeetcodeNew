"""
1590. Make Sum Divisible by P
"""
class Solution:
    def minSubarray(self, nums, p: int) -> int:
        total = sum(nums)
        modu = total % p
        if modu in nums:
            return 1
        elif modu == 0:
            return 0
        nums.sort()
        for num in nums:
            pass




# assert Solution().minSubarray([3,1,4,2], 6) == 1
assert Solution().minSubarray([6,3,5,2], 9) == 2
# assert Solution().minSubarray([1,2,3], 3) == 0
# assert Solution().minSubarray([1,2,3], 7) == -1