"""
424. Longest Repeating Character Replacement
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(max_count, count[s[r]])

            # If window is invalid, shrink from left
            while (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


assert Solution().characterReplacement("ABAB", 2) == 4
assert Solution().characterReplacement("AABABBA", 1) == 4
assert Solution().characterReplacement("AAAA", 2) == 4
assert Solution().characterReplacement("ABCDE", 1) == 2
assert Solution().characterReplacement("A", 0) == 1
assert Solution().characterReplacement("AAAB", 0) == 3

