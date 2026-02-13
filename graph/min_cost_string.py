"""
2976. Minimum Cost to Convert String I
"""
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        n = 26
        
        # Step 1: initialize cost matrix
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Step 2: fill direct transformations
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        # Step 3: Floyd–Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
        
        # Step 4: calculate answer
        total = 0
        for s, t in zip(source, target):
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]
        
        return total

# Example usage
if __name__ == "__main__":  
    solution = Solution()
    # source = "abc"
    # target = "bcd"
    # original = ["a", "b", "c"]
    # changed = ["b", "c", "d"]
    # cost = [1, 1, 1]
    # print(solution.minimumCost(source, target, original, changed, cost))  # Output: 3

     
    source = "abcd"
    target = "acbe"
    original = ["a","b","c","c","e","d"]
    changed = ["b","c","b","e","b","e"]
    cost = [2,5,5,1,2,20]
    print(solution.minimumCost(source, target, original, changed, cost))  # Output: 28
