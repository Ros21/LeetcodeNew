"""
1458. Max Dot Product of Two Subsequences
"""
from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[float("-inf")]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j]=nums1[i]*nums2[j]
                if i>0 and j>0:
                    dp[i][j]=max(dp[i][j], dp[i][j]+ dp[i-1][j-1])
                if i>0:
                    dp[i][j]=max(dp[i][j], dp[i-1][j])
                if j>0:
                    dp[i][j]=max(dp[i][j], dp[i][j-1])

        return dp[m-1][n-1]

print(Solution().maxDotProduct([2,1,-2,5], [3,0,-6])) #== 18
print(Solution().maxDotProduct([3,-2], [2,-6,7])) #== 21