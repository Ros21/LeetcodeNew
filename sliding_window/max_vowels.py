"""
1456. Maximum Number of Vowels in a Substring of Given Length
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        count = 0
        max_count =0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        max_count = max(max_count, count)
        
        for j in range(k, len(s)):
            if s[j] in vowels:
                count+=1
            if s[j-k] in vowels:
                count-=1
            max_count = max(max_count, count)
        return max_count


assert Solution().maxVowels("abciiidef", 3) == 3
assert Solution().maxVowels("aeiou", 2) == 2
assert Solution().maxVowels("leetcode", 3) == 2
assert Solution().maxVowels("rhythms", 4) == 0
assert Solution().maxVowels("weallloveyou", 7) == 4
