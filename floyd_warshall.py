def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {i: {j: float('inf') for j in nodes} for i in nodes}

    for node in nodes:
        dist[node][node] = 0

    for u, v, w in graph:
        dist[u][v] = w

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

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

print("Floyd-Warshall Algorithm:", floyd_warshall(edges_example))
