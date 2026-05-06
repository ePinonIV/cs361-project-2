# Code to implement Version 2: Priority Queue Dijkstra
# minimum distance vertex is selected using min-priority queue  
# - expected time complexity: O((V + E) log(V) )

import sys
import heapq
from graph_setup import (sparse1, sparse2, dense1, dense2, dense3, benchmark_print, char_map, int_map)

# ----- dijkstra's implementation -----

def dijkstra_pq(graph, start):
    V = graph.V
    pq = []
    dist = {}
    parent = {}
    
    # initialize distances as infinity and no parents
    for i in range(V):
        dist[i] = sys.maxsize
        parent[i] = None
    
    # init heap with start node
    dist[start] = 0
    heapq.heappush(pq, (0, start))
    
    # process queue until all neighbors finalized
    while pq:
        cur_dist, u = heapq.heappop(pq)

        if dist[u] < cur_dist:
            continue

        # explore neighbors of current v
        cur_neighbors = graph.list[u]

        for v, w in cur_neighbors:
            new_dist = cur_dist + w

            # relaxation - check if new path is shorter
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, parent

# ----- run benchmarking -----

def main():

    #graphs for testing
    sparse_graphs = [
        (sparse1, char_map['A']),
        (sparse2, int_map['1'])
    ]
    dense_graphs = [
        (dense1, char_map['A']),
        (dense2, int_map['1']),
        (dense3, int_map['1'])
    ]

    print("Version 2: Priority Queue Dijkstra\n")

    print("Priority Queue (Sparse Graphs)\n")
    for i, start in sparse_graphs:
        benchmark_print(dijkstra_pq, i, start)
        print("------------------------------------------")

    print("Priority Queue (Dense Graphs)\n")
    for i, start in dense_graphs:
        benchmark_print(dijkstra_pq, i, start)
        print("------------------------------------------")



if __name__ == "__main__":
    main()