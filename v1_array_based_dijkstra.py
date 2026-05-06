# Code to implement Version 1: Array-Based Dijkstra
# the algorithm stores distances in an array and
# repeatedly scans (explores) all unvisited vertices
# to find the vertex with the current smallest distance

import sys
from graph_setup import (sparse1, sparse2, dense1, dense2, dense3, benchmark_print, char_map, int_map)


def dijkstra_array_list(graph, start):
    V = graph.V
    dist = {}
    parent = {}

    #set all dist to infinity
    for i in range(V):
        dist[i] = sys.maxsize
        parent[i] = None
    
    #start dist at 0
    dist[start] = 0
    visited = set()

    #loop to find the shortest path
    for _ in range(V):
        min_dist = sys.maxsize
        #unvisted node with closest distance
        u = -1

        #find unvisited vertex with min dist
        for i in range(V):
            if i not in visited and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        #stop if all unvisted vertice dist is inf
        if u == -1:
            break

        visited.add(u)

        #update the neighbors
        for v, weight in graph.list[u]:
            if v not in visited:
                new_dist = dist[u] + weight
                #update new shortest dist
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
    
    return dist, parent


def dijkstra_array_matrix(graph, start):
    V = graph.V
    dist = {}
    parent = {}

    #set all dist to infinity
    for i in range(V):
        dist[i] = sys.maxsize
        parent[i] = None
    
    #start dist at 0
    dist[start] = 0
    visited = set()

    #loop to find the shortest path
    for _ in range(V):
        min_dist = sys.maxsize
        #unvisted node with closest distance
        u = -1

        #find unvisited vertex with min dist
        for i in range(V):
            if i not in visited and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        #stop if all unvisted vertice dist is inf
        if u == -1:
            break

        visited.add(u)

        #update the neighbors
        for v in range(V):
            weigth = graph.mat[u][v]
            #checks if edge exists and if vertex is unvisted
            if weigth > -1 and v not in visited:
                new_dist = dist[u] + weigth
                #update new shortest dist
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
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

    print("Version 1: Array Based Dijkstra\n")

    print("Adjancency List\n")
    for i, start in sparse_graphs:
        benchmark_print(dijkstra_array_list, i, start)
        print("------------------------------------------")

    print("Adjancency Matrix\n")
    for i, start in dense_graphs:
        benchmark_print(dijkstra_array_matrix, i, start)
        print("------------------------------------------")


if __name__ == "__main__":
    main()