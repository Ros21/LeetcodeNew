"""
40. Combination Sum II
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, path):
            if sum(path)==target and path not in result:
                result.append(path[:])
                return 
            if sum(path)>target:
                return
            
            for i in range(start,len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1,path)
                path.pop()
        
        backtrack(0, [])
        return result


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8)) 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]