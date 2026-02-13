"""
131. Palindrome Partitioning
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(substring):
            return substring==substring[::-1]


        def backtrack(start,path):
            if len(s)==start:
                result.append(path[:])
                return
            
            for end in range(start+1, len(s)+1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end,path)
                    path.pop()

        backtrack(0,[])
        return result


print(Solution().partition("aab"))  # [["a","a","b"],["aa","b"]]
print(Solution().partition("a"))  # [["a"]]
print(Solution().partition("efe"))  # [["e","f","e"],["efe"]]
print(Solution().partition("racecar"))  # [["r","a","c","e","c","a","r"],["r","a","cec","a","r"],["r","aceca","r"],["racecar"]]

