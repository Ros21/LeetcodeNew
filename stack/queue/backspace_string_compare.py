"""
844. Backspace String Compare
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack=[]
            for ch in string:
                if ch=="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)

        return build(s)==build(t)
 

assert Solution().backspaceCompare("ab#c", "ad#c") == True
assert Solution().backspaceCompare("ab##", "c#d#") == True
assert Solution().backspaceCompare("a##c", "#a#c") == True
assert Solution().backspaceCompare("a#c", "b") == False
assert Solution().backspaceCompare("xy#z", "xzz#") == True
assert Solution().backspaceCompare("xp#", "xyz##") == True
assert Solution().backspaceCompare("y#fo##f", "y#f#o##f") == True

