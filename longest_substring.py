class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        left =0
        right = 1
        while right<len(s):
            pass


print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
print(Solution().lengthOfLongestSubstring(""))  # 0
print(Solution().lengthOfLongestSubstring("a"))  # 1
print(Solution().lengthOfLongestSubstring("dvdf"))  # 3
print(Solution().lengthOfLongestSubstring("anviaj"))  # 5