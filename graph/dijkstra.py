"""
Dijkstra’s algorithm
"""
import heapq
from collections import defaultdict

def dijkstra(n, edges, src):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    print(f"graph={graph}")

    # Distance array
    dist = [float('inf')] * n
    dist[src] = 0

    # Min-heap: (distance, node)
    pq = [(0, src)]

    while pq:
        cur_dist, u = heapq.heappop(pq)

        # Skip outdated entries
        if cur_dist > dist[u]:
            continue

        for v, w in graph[u]:
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist

n = 5
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3),
    (3, 4, 1)
]

print(dijkstra(n, edges, 0))