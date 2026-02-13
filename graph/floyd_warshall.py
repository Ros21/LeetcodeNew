def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find the shortest paths
    between all pairs of vertices in a weighted graph.

    :param graph: A 2D list (matrix) representing the adjacency matrix of the graph.
                  Use float('inf') to represent no direct path between vertices.
    :return: A 2D list representing the shortest path distances between all pairs of vertices.
    """
    num_vertices = len(graph)
    # Initialize distance matrix with the input graph's weights
    distance = [[graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    # Update the distance matrix with shortest paths
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

# Example usage
if __name__ == "__main__":
    inf = float('inf')
    graph = [
        [0, 3, inf, 7],
        [8, 0, 2, inf],
        [5, inf, 0, 1],
        [2, inf, inf, 0]
    ]

    shortest_paths = floyd_warshall(graph)
    for row in shortest_paths:
        print(row)