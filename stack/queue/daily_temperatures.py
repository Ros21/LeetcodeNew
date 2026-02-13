"""
739. Daily Temperatures
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)

        for index,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                popped=stack.pop()
                result[popped] = index - popped
            stack.append(index)
        return result


assert Solution().dailyTemperatures([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert Solution().dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert Solution().dailyTemperatures([30,60,90]) == [1,1,0]  
