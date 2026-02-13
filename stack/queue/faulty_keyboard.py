"""
2810. Faulty Keyboard
"""
class Solution:
    def finalString(self, s: str) -> str:
        if not "i" in s:
            return s
        result=""
        for ch in s:
            if ch=="i":
                result= result[::-1]
            else:
                result+=ch
        return result
                


assert Solution().finalString("string") == "rtsng"
assert Solution().finalString("poiinter") == "ponter"
assert Solution().finalString("abc") == "abc"
