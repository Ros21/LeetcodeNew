"""
516. Longest Palindromic Subsequence
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev_s = s[::-1]
        m = len(s)
        n = len(rev_s)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1, n+1):
                if s[i-1]==rev_s[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]


print(Solution().longestPalindromeSubseq("bbbab")) #4