"""
22. Generate Parentheses
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        close<=start
        start<=len(n)
        """
        path = []
        result = []
        def backtrack(start,close):
            if start==close==n:
                result.append("".join(path))
                return 
            if start<n:
                path.append("(")
                backtrack(start+1,close)
                path.pop()
            if close<start:
                path.append(")")
                backtrack(start,close+1)
                path.pop()

        backtrack(0,0)
        return result


print((Solution().generateParenthesis(n=3))) #==["((()))","(()())","(())()","()(())","()()()"]
# assert(Solution().generateParenthesis(n=1))==["()"]
# assert(Solution().generateParenthesis(n=2))==["(())","()()"]
# assert(Solution().generateParenthesis(n=0))==[""]
