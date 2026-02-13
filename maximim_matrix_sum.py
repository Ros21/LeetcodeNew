"""
1975. Maximum Matrix Sum
"""
class Solution:
    def maxMatrixSum(self, matrix) -> int:
        total = 0
        negatives = 0
        min_value = float("inf")
        for row in matrix:
            for n in row:
                total+=abs(n)
                if n<0:
                    negatives+=1
                min_value= min(min_value, abs(n))
        if negatives%2==1:
            total-=2*min_value
        return total


print(Solution().maxMatrixSum([[1,-1],[-1,1]])) #4
print(Solution().maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])) #16
print(Solution().maxMatrixSum([[-1,0,-1],[-2,1,3],[3,2,2]])) #15

