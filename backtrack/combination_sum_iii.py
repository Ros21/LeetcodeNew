"""
216. Combination Sum III
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(start,path,remaining_sum):
            if len(path)==k and remaining_sum==0 :
                # sorted_path = sorted(path[:])
                result.append(path[:])
                return
            
            if remaining_sum<0 or len(path)>k:
                return
            
            for num in range(start,10):
                path.append(num)
                backtrack(num+1,path, remaining_sum-num)
                path.pop()

            
        backtrack(1,[],n)
        return result


print(Solution().combinationSum3(3, 7)) # ==[[1,2,4]]
# print(Solution().combinationSum3(3, 9)) # ==[[1,2,6],[1,3,5],[2,3,4]]
# print(Solution().combinationSum3(4, 1)) # ==[]