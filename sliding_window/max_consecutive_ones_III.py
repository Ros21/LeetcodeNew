"""
1004. Max Consecutive Ones III
"""
class Solution:
    def longestOnes(self, nums, k: int) -> int:
        left = 0
        max_count = 0
        num_zeros = 0
        for right in range(len(nums)):
            if nums[right]==0:
                num_zeros+=1

            while num_zeros>k:
                if nums[left]==0:
                    num_zeros-=1
                left+=1

            max_count= max(max_count, right-left+1)
        return max_count
                

assert Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
assert Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
assert Solution().longestOnes([1,1,1,1], 0) == 4
