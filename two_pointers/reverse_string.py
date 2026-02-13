"""
344. Reverse String
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)
        while i<j:
            s[i],s[j-1]=s[j-1],s[i]
            i+=1
            j-=1
        return s

assert Solution().reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
assert Solution().reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"] 


