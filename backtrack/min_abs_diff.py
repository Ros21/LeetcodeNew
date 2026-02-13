"""
1200. Minimum Absolute Difference
"""
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = []
        min_value = arr[1]-arr[0]
        for index in range(1, len(arr)-1):
            current_diff = abs(arr[index+1]-arr[index])
            min_value = min(min_value,current_diff )
        
        for index in range(len(arr)-1):
            if abs(arr[index+1]-arr[index]) == min_value:
                min_diff.append([arr[index],arr[index+1]])
        return min_diff
    

print(Solution().minimumAbsDifference([4,2,1,3])) # [[1,2],[2,3],[3,4]]
print(Solution().minimumAbsDifference([1,3,6,10,15])) # [[1,3]]
print(Solution().minimumAbsDifference([3,8,-10,23,19,-42,-14,27])) # [[-14,-10],[19,23],[23,27]]