"""
Docstring for graph.min_dist
"""
from collections import deque
from typing import List

import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))        # normal edge
            graph[v].append((u, 2 * w))    # reversed edge

        dist = [float('inf')] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            if u == n - 1:
                return cost
            
            print(graph)
            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1



print(Solution().minCost(n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]))  # 3
print(Solution().minCost(n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]))  # 5
