"""
2435. Paths in Matrix Whose Sum Is Divisible by K
"""
class Solution:
    def numberOfPaths(self, grid, k: int) -> int:
        self.result = 0
        def backtrack(path):
            if sum(path)%k==0:
                self.result+=1 
                return
            for i in range(len(grid)):
                for j in range(len(grid(0))):
                    path.append(grid[i][j])
                    backtrack(path)
                    path.pop()
            
        backtrack([])
        return self.result



assert Solution().numberOfPaths([[5,2,4],[3,0,5],[0,7,2]], 3) == 2
assert Solution().numberOfPaths([[0,0]], 5) == 1
assert Solution().numberOfPaths([[7,3,4,5],[2,3,6,7],[2,1,3,4],[5,0,2,6]], 3) == 4
assert Solution().numberOfPaths([[1,2,3],[4,5,6]], 3) == 0