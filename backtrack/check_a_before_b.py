"""
2124. Check if All A's Appears Before All B's
"""
class Solution:
    def checkString(self, s: str) -> bool:
        l = len(s)
        i =0
        while i<l and s[i]!='b':
            i+=1
        for j in range(i+1,len(s)):
            if s[j]!='b':
                return False
        return True

print(Solution().checkString("aaabbb")) # ==True
print(Solution().checkString("abab")) # ==False
print(Solution().checkString("bbb")) # ==True