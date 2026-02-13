"""
2011. Final Value of Variable After Performing Operations
"""
from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # x=0
        return sum(1 if "++" in op else -1 for op in operations)
        # for operation in operations:
            # if "++" in operation:
            #     x=x+1
            # else:
            #     x=x-1
        # return x


assert Solution().finalValueAfterOperations(["--X","X++","X++"])==1
assert Solution().finalValueAfterOperations(["++X","++X","X++"])==3     
assert Solution().finalValueAfterOperations(["X++","++X","--X","X--"])==0
assert Solution().finalValueAfterOperations(["X++","X++","X++"])==3
assert Solution().finalValueAfterOperations(["--X","--X","--X"])==-3
assert Solution().finalValueAfterOperations(["++X","--X","++X","--X"])==0
assert Solution().finalValueAfterOperations([])==0