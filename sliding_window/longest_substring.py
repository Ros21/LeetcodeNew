"""
3. Longest Substring Without Repeating Characters
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "abcabcbb"
        """
        left = 0
        result = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            result = max(result,right-left+1)
        return result


assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("") == 0
assert Solution().lengthOfLongestSubstring(" ") == 1
assert Solution().lengthOfLongestSubstring("aab") == 2
