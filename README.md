# Shortest Path Graph Algorithms

This repository contains Python implementations of three fundamental graph algorithms:

1. **Dijkstra's Algorithm** - Single-source shortest path for graphs with non-negative edge weights.
2. **Bellman-Ford Algorithm** - Single-source shortest path that handles graphs with negative edge weights.
3. **Floyd-Warshall Algorithm** - All-pairs shortest path using dynamic programming.

All implementations include test cases based on examples from the book *Introduction to Algorithms, Third Edition* by Thomas H. Cormen et al.

---

## Algorithms

### 1. Dijkstra's Algorithm
Dijkstra's algorithm computes the shortest path from a single source node to all other nodes in a graph with non-negative edge weights.

#### Implementation
The algorithm uses a priority queue (min-heap) to select the next node with the smallest tentative distance.

#### Dijkstra

```plaintext
s --10--> t
s --5--> y
t --1--> x
t --2--> y
y --9--> x
y --3--> t
y --2--> z
z --7--> s
z --6--> x
{'s': 0, 't': 8, 'x': 14, 'y': 5, 'z': 7}
```
### Bellman-Ford
```
s --6--> t
s --7--> y
t --5--> x
t --8--> y
t ---4--> z
y --9--> z
y ---3--> x
z --7--> x
x ---2--> t
{'s': 0, 't': 6, 'x': 4, 'y': 7, 'z': 2}
```
### Floyd-Warshall
```
s --6--> t
s --7--> y
t --5--> x
t --8--> y
t ---4--> z
y --9--> z
y ---3--> x
z --7--> x
x ---2--> t
{
    's': {'s': 0, 't': 6, 'y': 7, 'z': 2, 'x': 4},
    't': {'s': inf, 't': 0, 'y': 8, 'z': -4, 'x': 5},
    'y': {'s': inf, 't': 8, 'y': 0, 'z': 9, 'x': -3},
    'z': {'s': 7, 't': 8, 'y': inf, 'z': 0, 'x': 7},
    'x': {'s': inf, 't': -2, 'y': inf, 'z': inf, 'x': 0}
}

```

