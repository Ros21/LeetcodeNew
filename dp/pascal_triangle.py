"""
118. Pascal's Triangle
"""
class Solution:
    def generate(self, numRows):
        triangle = []
        for r in range(0, numRows):
            row = [1]*(r+1)
            for col in range(1,r):
                row[col] = triangle[r-1][col-1] + triangle[r-1][col]
            triangle.append(row)
        return triangle


            



print(Solution().generate(5))
