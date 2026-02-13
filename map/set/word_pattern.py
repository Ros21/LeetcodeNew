"""
290. Word Pattern
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(s_list)!=len(pattern):
            return False
        result = {}
        for i in range(len(pattern)):
            if pattern[i] in result and result[pattern[i]]!=s_list[i]:
                return False
            else:
                result[pattern[i]] =  s_list[i]
        if len(result.values())!=len(set(result.values())):
            return False
        return True


assert Solution().wordPattern("abba", "dog cat cat dog")==True
assert Solution().wordPattern("abba", "dog cat cat fish")==False
assert Solution().wordPattern("abba", "dog dog dog dog")==False
assert Solution().wordPattern("aaaa", "dog cat cat dog")==False
assert Solution().wordPattern("aba", "cat cat cat dog")==False