from typing import List
# Single Source Shortest Path algorithm that applies to non-negative weight
# Time complexity of O(E * logV) if implemented with min-heap, and O (V ** 2) if implemented with matrix

# Method 1: O (V ** 2) Implementation
def findShortestPath(totalNodes:int, costs:List[List[int]], target:int, source:int) -> int:
    d = [float('inf') for i in range(totalNodes)] # d[i] represents shortest distance between source to i
    visited = set()
    d[source] = 0

    while True:
        # find the smallest edge that is not in visited
        v = -1
        for u in range(totalNodes):
            if u not in visited and (v == -1 or d[u] < d[v]):
                v = u

        if v == -1:
            break
        visited.add(v)

        # add the smallest edge to visited and update all other nodes not in visited
        for u in range(totalNodes):
            if u not in visited:
                d[u] = min(d[u], d[v] + costs[u][v])
    
    return d[target]

# Method 2: O (E * logV) Implementation
def findShortestPathWithHeap(totalNodes:int, costs:List[List[int]], target:int, source:int) -> int:
    d = [float('inf') for i in range(totalNodes)] # d[i] represents shortest distance between source to i
    unvisitedArr = [(0, source)]
    visited = set()
    d[0] = 0

    while unvisitedArr and target not in visited:
        (dv, v) = heapq.heappop(unvisitedArr)
        if v in visited or dv > d[v]:
            continue
        visited.add(v)
        # update all other nodes in unvisited min heap 
        for u in range(totalNodes):
            if d[u] > d[v] + costs[u][v]:
                d[u] = d[v] + costs[u][v]
                heapq.heappush(unvisitedArr, (d[u], u))
    return d[target]

# Test
total = 6
target = 5
source = 0 
INF = float('inf')
costs = [[0, INF, INF, INF, INF, INF],
         [3, 0, INF, INF, INF, 3],
         [1, 2, 0, INF, INF, INF],
         [1, INF, INF, 0, INF, INF],
         [INF, INF, 1, INF, 1, INF],
         [INF, INF, INF, INF, 2, 0]]
print('res: ', findShortestPath(total, costs, target, source))
