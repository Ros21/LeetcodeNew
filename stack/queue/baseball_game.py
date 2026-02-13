"""
682. Baseball Game
"""
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for op in operations:
            if op=="D":
                stack.append(stack[-1]*2)
            elif op=="C":
                stack.pop()
            elif op=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)




assert Solution().calPoints(["5","2","C","D","+"]) == 30
assert Solution().calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert Solution().calPoints(["1"]) == 1 
assert Solution().calPoints(["10","-10","D","C","+"]) == 0

