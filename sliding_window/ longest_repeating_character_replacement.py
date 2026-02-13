"""
424. Longest Repeating Character Replacement
"""
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_count = {}
        result = 0
        max_count = 0
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right],0)+1
            max_count = max(max_count, char_count[s[right]])
            while (right-left+1)-max_count>k:
                char_count[s[left]] -= 1
                left+=1
        
        result = max(result, right-left+1)
        return result



# assert Solution().characterReplacement("ABAB", 2) == 4
assert Solution().characterReplacement("AABABBA", 1) == 4
# assert Solution().characterReplacement("AAAA", 2) == 4
# assert Solution().characterReplacement("ABCDE", 1) == 2
# assert Solution().characterReplacement("AAAB", 0) == 3