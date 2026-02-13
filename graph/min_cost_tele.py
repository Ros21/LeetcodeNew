"""
3651. Minimum Cost Path with Teleportations
"""
import heapq
from typing import List
from math import inf


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # dist[t][i][j]
        dist = [[[inf] * n for _ in range(m)] for _ in range(k + 1)]
        dist[0][0][0] = 0

        # All cells sorted by value
        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))

        # One pointer per teleport layer
        ptr = [0] * (k + 1)

        pq = [(0, 0, 0, 0)]  # cost, i, j, teleports_used

        while pq:
            cost, i, j, t = heapq.heappop(pq)

            if cost > dist[t][i][j]:
                continue

            if i == m - 1 and j == n - 1:
                return cost

            # Normal moves
            for ni, nj in ((i + 1, j), (i, j + 1)):
                if ni < m and nj < n:
                    nc = cost + grid[ni][nj]
                    if nc < dist[t][ni][nj]:
                        dist[t][ni][nj] = nc
                        heapq.heappush(pq, (nc, ni, nj, t))

            # Teleport moves
            if t < k:
                v = grid[i][j]
                p = ptr[t]

                while p < len(cells) and cells[p][0] <= v:
                    _, x, y = cells[p]
                    if cost < dist[t + 1][x][y]:
                        dist[t + 1][x][y] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
                    p += 1

                ptr[t] = p

        return -1

print(Solution().minCost([[5,1,2],[4,0,3],[7,8,6]], 1))  # 6
print(Solution().minCost([[5,1,2],[4,0,3],[7,8,6]], 2))  # 6
print(Solution().minCost([[1,2,3],[4,5,6],[7,8,9]], 1))  # 19
