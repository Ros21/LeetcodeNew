"""
76. Minimum Window Substring
"""
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left = 0
        count_t={}
        for ch in t:
            count_t[ch] = count_t.get(ch,0)+1
        result = [-1,-1]
        max_len= float("infinity")
        count_s= {}
        have, need = 0, len(count_t)

        for right in range(len(s)):
            ch = s[right]
            count_s[ch] = count_s.get(ch,0)+1

            if ch in count_t and count_s[ch]==count_t[ch]:
                have+=1

            while have==need:
                if (right-left+1) < max_len:
                    result = [left,right]
                    max_len = right-left+1

                count_s[s[left]]-=1

                if s[left] in count_t and count_s[s[left]]<count_t[s[left]]:
                    have-=1
                left+=1
        left, right = result
        
        return s[left:right+1] if max_len!=float("infinity") else ""



assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert Solution().minWindow("a", "a") == "a"
assert Solution().minWindow("a", "aa") == ""
assert Solution().minWindow("ab", "A") == ""
assert Solution().minWindow("a", "b") == ""
assert Solution().minWindow("aa", "aa") == "aa"