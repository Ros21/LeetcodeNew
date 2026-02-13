"""
198. House Robber
"""
class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(dp[1], nums[1])

        for i in range(2,n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]

# print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))

# [3,2,3,1,2,4,5,5,6]
# [1,2,2,3,3,4,5,5,6]