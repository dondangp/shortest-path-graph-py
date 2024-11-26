def bellman_ford(graph, vertices, start):
    dist = {node: float('inf') for node in vertices}
    dist[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative-weight cycles
    for u, v, w in graph:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist

# Example test
edges_example = [
    ('s', 't', 6),
    ('s', 'y', 7),
    ('t', 'x', 5),
    ('t', 'y', 8),
    ('t', 'z', -4),
    ('y', 'z', 9),
    ('y', 'x', -3),
    ('z', 'x', 7),
    ('x', 't', -2),
]

vertices_example = ['s', 't', 'x', 'y', 'z']

print("Bellman-Ford Algorithm:", bellman_ford(edges_example, vertices_example, 's'))
