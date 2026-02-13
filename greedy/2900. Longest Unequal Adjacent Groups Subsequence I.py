"""
2900. Longest Unequal Adjacent Groups Subsequence I
"""
class Solution:
    def getLongestSubsequence(self, words, group):
        last_group = None
        res = []
        for ch, g in zip(words,group):
            if g != last_group:
                res.append(ch)
                last_group = g
        return res



print(Solution().getLongestSubsequence(words = ["e","a","b"], group = [0,0,1])) 
#["e","b"]