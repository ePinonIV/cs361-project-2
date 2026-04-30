# - Defines graph class that can be used to store graphs represented in adjacency lists or matrices
# - Creates all graphs that we will run the algorithms on, based on the given images
# - Has benchmark wrapper to run any algorithm with a given graph and report run time and memory usage

import time
import tracemalloc

# -----  -----
char_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
int_map = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8}

# wrapper to run with algorithm for a given graph and find the run time and memory
def benchmark_print(algo, graph, start):
    times = []
    mem_usages = []
    
    for i in range(5):
        tracemalloc.start()

        start_time = time.perf_counter()
        path = algo(graph, start)
        end_time = time.perf_counter()

        i, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times.append(end_time - start_time)
        mem_usages.append(peak_mem)
    
    avg_time = sum(times) / 5
    avg_mem = sum(mem_usages) / 5

    print("Benchmark for Graph " + graph.name + ":")
    print("Path taken: " + str(path))
    print("Average runtime = " + str(avg_time))
    print("Average memory usage = " + str(avg_mem))
    #return path, avg_time, avg_mem


# ----- Graph Class Implementation -----

class Graph:
    def __init__(self, name, num_nodes):
        self.name = name
        self.V = num_nodes
        self.E = 0 
        self.type = type
        self.list = [[] for n in range(num_nodes)]
        self.mat = [[-1 for n in range(num_nodes)] for n in range(num_nodes)]

    def add_edge(self, v1, v2, w):
        # add to adjacency list
        if v2 not in self.list[v1]:
            self.list[v1].append((v2,w))
            self.list[v2].append((v1,w))
        # add to adjacency matrix
        if self.mat[v1][v2] == -1:
            self.mat[v1][v2] = w
            self.mat[v2][v1] = w
        self.E += 1

    def gprint(self):
        print("Printing Graph " + self.name + " Info...")
        print("# Vertices = " + str(self.V))
        print("# Edges = " + str(self.E))
        print("Adjacency List:")
        for i in range(self.V):
            print(str(self.list[i]))
        print("Adjacency Matrix:")
        for i in range(self.V):
            print(str(self.mat[i]))
        print("..............................\n")
        
    def explore(self, v, type):
        neighbors = []
        if type == 'list':
            neighbors.append(v)
            neighbors.append(v+1)
        elif type == 'matrix':
            for i in range(self.V):
                if self.mat[v][i] > -1:
                    neighbors.append(i)
        return neighbors



# ---------- Create graphs ----------

# sparse graphs

sparse1 = Graph("Sparse 1", 6)
sparse1.add_edge(char_map['A'],char_map['B'],4)
sparse1.add_edge(char_map['A'],char_map['C'],2)
sparse1.add_edge(char_map['B'],char_map['D'],5)
sparse1.add_edge(char_map['C'],char_map['D'],1)
sparse1.add_edge(char_map['D'],char_map['E'],3)
sparse1.add_edge(char_map['E'],char_map['F'],2)

sparse2 = Graph("Sparse 2", 7)
sparse2.add_edge(int_map['1'],int_map['2'],3)
sparse2.add_edge(int_map['1'],int_map['3'],6)
sparse2.add_edge(int_map['2'],int_map['4'],2)
sparse2.add_edge(int_map['3'],int_map['5'],4)
sparse2.add_edge(int_map['4'],int_map['6'],7)
sparse2.add_edge(int_map['5'],int_map['7'],1)
sparse2.add_edge(int_map['2'],int_map['5'],5)

# dense graphs 

dense1 = Graph("Dense 1", 5)
dense1.add_edge(char_map['A'],char_map['B'],2)
dense1.add_edge(char_map['A'],char_map['C'],5)
dense1.add_edge(char_map['A'],char_map['D'],1)
dense1.add_edge(char_map['A'],char_map['E'],4)
dense1.add_edge(char_map['B'],char_map['C'],3)
dense1.add_edge(char_map['B'],char_map['D'],2)
dense1.add_edge(char_map['B'],char_map['E'],6)
dense1.add_edge(char_map['C'],char_map['D'],3)
dense1.add_edge(char_map['C'],char_map['E'],1)
dense1.add_edge(char_map['D'],char_map['E'],2)

dense2 = Graph("Dense 2", 6)
dense2.add_edge(int_map['1'],int_map['2'],3)
dense2.add_edge(int_map['1'],int_map['3'],2)
dense2.add_edge(int_map['1'],int_map['4'],6)
dense2.add_edge(int_map['1'],int_map['5'],5)
dense2.add_edge(int_map['1'],int_map['6'],4)
dense2.add_edge(int_map['2'],int_map['3'],1)
dense2.add_edge(int_map['2'],int_map['4'],2)
dense2.add_edge(int_map['2'],int_map['5'],4)
dense2.add_edge(int_map['2'],int_map['6'],7)
dense2.add_edge(int_map['3'],int_map['4'],3)
dense2.add_edge(int_map['3'],int_map['5'],6)
dense2.add_edge(int_map['3'],int_map['6'],5)
dense2.add_edge(int_map['4'],int_map['5'],2)
dense2.add_edge(int_map['4'],int_map['6'],4)
dense2.add_edge(int_map['5'],int_map['6'],1)

dense3 = Graph("Dense 3", 7)
dense3.add_edge(int_map['1'],int_map['2'],5)
dense3.add_edge(int_map['1'],int_map['3'],6)
dense3.add_edge(int_map['1'],int_map['4'],8)
dense3.add_edge(int_map['1'],int_map['5'],2)
dense3.add_edge(int_map['1'],int_map['6'],4)
dense3.add_edge(int_map['1'],int_map['7'],4)
dense3.add_edge(int_map['2'],int_map['3'],3)
dense3.add_edge(int_map['2'],int_map['4'],2)
dense3.add_edge(int_map['2'],int_map['5'],6)
dense3.add_edge(int_map['2'],int_map['6'],1)
dense3.add_edge(int_map['3'],int_map['4'],2)
dense3.add_edge(int_map['3'],int_map['5'],8)
dense3.add_edge(int_map['3'],int_map['6'],2)
dense3.add_edge(int_map['3'],int_map['7'],7)
dense3.add_edge(int_map['4'],int_map['5'],6)
dense3.add_edge(int_map['4'],int_map['6'],9)
dense3.add_edge(int_map['4'],int_map['7'],3)
dense3.add_edge(int_map['5'],int_map['6'],9)
dense3.add_edge(int_map['5'],int_map['7'],1)
dense3.add_edge(int_map['6'],int_map['7'],2)

# print graphs to verify correctness
def main():
    sparse1.gprint()
    sparse2.gprint()
    dense1.gprint()
    dense2.gprint()
    dense3.gprint()

if __name__ == "__main__":
    main()