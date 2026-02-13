"""
387. First Unique Character in a String
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for ch in s:
            char_count[ch]=char_count.get(ch,0)+1

        for i, ch in enumerate(s):
            if char_count[ch]==1:
                return i
        return -1

assert Solution().firstUniqChar("leetcode") == 0
assert Solution().firstUniqChar("loveleetcode") == 2
assert Solution().firstUniqChar("aabb") == -1
assert Solution().firstUniqChar("z") == 0
assert Solution().firstUniqChar("dddccdbba") == 8
assert Solution().firstUniqChar("abcabc") == -1
