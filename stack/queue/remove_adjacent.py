"""
1047. Remove All Adjacent Duplicates In String
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack =[]
        for ch in s:
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


assert Solution().removeDuplicates("abbaca") == "ca"
assert Solution().removeDuplicates("azxxzy") == "ay"
assert Solution().removeDuplicates("a") == "a"
assert Solution().removeDuplicates("aa") == ""
assert Solution().removeDuplicates("aab") == "b"
assert Solution().removeDuplicates("abba") == ""
assert Solution().removeDuplicates("abccba") == ""
assert Solution().removeDuplicates("abcddcba") == ""
assert Solution().removeDuplicates("aabbccddeeff") == ""