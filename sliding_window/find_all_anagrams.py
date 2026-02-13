"""
438. Find All Anagrams in a String
"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        result = []
        sorted_p = ''.join(sorted(p))
        k = len(sorted_p)
        for i in range(len(s)-k+1):
            sorted_sub = ''.join(sorted(s[i:k+i]))
            if sorted_sub==sorted_p:
                result.append(i)
        return result


assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]
assert Solution().findAnagrams("abab", "ab") == [0, 1, 2]
assert Solution().findAnagrams("af", "be") == []