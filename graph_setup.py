# Defines graph class that can be used to store graphs represented in adjacency lists or matrices

class Graph:
    def __init__(self, num_nodes, type='list'):
        self.V = num_nodes
        self.E = 0 
        self.type = type
        if self.type == 'list':
            self.adj = [[] for n in range(num_nodes)]
        elif self.type == 'matrix':
            self.adj = [[-1 for n in range(num_nodes)] for n in range(num_nodes)]

    def add_edge(self, v1, v2, w):
        # adjacency list
        if self.type == 'list':
            if v2 not in self.adj[v1]:
                self.adj[v1].append(v2)
                self.adj[v1].append(w)
                self.adj[v2].append(v1)
                self.adj[v2].append(w)
        # adjacency matrix
        elif self.type == 'matrix':
            if self.adj[v1][v2] == 0:
                self.adj[v1][v2] = w
                self.adj[v2][v1] = w
        self.E += 1

    def explore(self, v):
        if self.type == 'list':
            return self.adj[v]
        elif self.type == 'matrix':
            neighbors = []
            for i in range(self.V):
                if self.adj[v][i] > -1:
                    neighbors.append(i)
            return neighbors

char_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

# ---------- Create graphs based on images ----------

# sparse graphs - only need lists

sg1 = Graph(6, 'list')
sg1.add_edge(char_map['A'],char_map['B'],4)
sg1.add_edge(char_map['A'],char_map['C'],2)
sg1.add_edge(char_map['B'],char_map['D'],5)
sg1.add_edge(char_map['C'],char_map['D'],1)
sg1.add_edge(char_map['D'],char_map['E'],3)
sg1.add_edge(char_map['E'],char_map['F'],2)

sg2 = Graph(6, 'list')
sg2.add_edge(1,2,3)
sg2.add_edge(1,3,6)
sg2.add_edge(2,4,2)
sg2.add_edge(3,5,4)
sg2.add_edge(4,6,7)
sg2.add_edge(5,7,1)
sg2.add_edge(2,5,5)

# dense graphs - need list and matrix versions

dg1_list = Graph(5, 'list')
dg1_list.add_edge(char_map['A'],char_map['B'],2)
dg1_list.add_edge(char_map['A'],char_map['C'],5)
dg1_list.add_edge(char_map['A'],char_map['D'],1)
dg1_list.add_edge(char_map['A'],char_map['E'],4)
dg1_list.add_edge(char_map['B'],char_map['C'],3)
dg1_list.add_edge(char_map['B'],char_map['D'],2)
dg1_list.add_edge(char_map['B'],char_map['E'],6)
dg1_list.add_edge(char_map['C'],char_map['D'],3)
dg1_list.add_edge(char_map['C'],char_map['E'],1)
dg1_list.add_edge(char_map['D'],char_map['E'],2)

dg1_mat = Graph(5, 'matrix')
dg1_mat.add_edge(char_map['A'],char_map['B'],2)
dg1_mat.add_edge(char_map['A'],char_map['C'],5)
dg1_mat.add_edge(char_map['A'],char_map['D'],1)
dg1_mat.add_edge(char_map['A'],char_map['E'],4)
dg1_mat.add_edge(char_map['B'],char_map['C'],3)
dg1_mat.add_edge(char_map['B'],char_map['D'],2)
dg1_mat.add_edge(char_map['B'],char_map['E'],6)
dg1_mat.add_edge(char_map['C'],char_map['D'],3)
dg1_mat.add_edge(char_map['C'],char_map['E'],1)
dg1_mat.add_edge(char_map['D'],char_map['E'],2)

dg2_list = Graph(6, 'list')
dg2_list.add_edge(1,2,3)
dg2_list.add_edge(1,3,2)
dg2_list.add_edge(1,4,6)
dg2_list.add_edge(1,5,5)
dg2_list.add_edge(1,6,4)
dg2_list.add_edge(2,3,1)
dg2_list.add_edge(2,4,2)
dg2_list.add_edge(2,5,4)
dg2_list.add_edge(2,6,7)
dg2_list.add_edge(3,4,3)
dg2_list.add_edge(3,5,6)
dg2_list.add_edge(3,6,5)
dg2_list.add_edge(4,5,2)
dg2_list.add_edge(4,6,4)
dg2_list.add_edge(5,6,1)

dg2_mat = Graph(6, 'mat')
dg2_mat.add_edge(1,2,3)
dg2_mat.add_edge(1,3,2)
dg2_mat.add_edge(1,4,6)
dg2_mat.add_edge(1,5,5)
dg2_mat.add_edge(1,6,4)
dg2_mat.add_edge(2,3,1)
dg2_mat.add_edge(2,4,2)
dg2_mat.add_edge(2,5,4)
dg2_mat.add_edge(2,6,7)
dg2_mat.add_edge(3,4,3)
dg2_mat.add_edge(3,5,6)
dg2_mat.add_edge(3,6,5)
dg2_mat.add_edge(4,5,2)
dg2_mat.add_edge(4,6,4)
dg2_mat.add_edge(5,6,1)

dg3_list = Graph(7, 'list')
dg3_list.add_edge(1,2,5)
dg3_list.add_edge(1,3,6)
dg3_list.add_edge(1,4,8)
dg3_list.add_edge(1,5,2)
dg3_list.add_edge(1,6,4)
dg3_list.add_edge(1,7,4)
dg3_list.add_edge(2,3,3)
dg3_list.add_edge(2,4,2)
dg3_list.add_edge(2,5,6)
dg3_list.add_edge(2,6,1)
dg3_list.add_edge(3,4,2)
dg3_list.add_edge(3,5,8)
dg3_list.add_edge(3,6,2)
dg3_list.add_edge(3,7,7)
dg3_list.add_edge(4,5,6)
dg3_list.add_edge(4,6,9)
dg3_list.add_edge(4,7,3)
dg3_list.add_edge(5,6,9)
dg3_list.add_edge(5,7,1)
dg3_list.add_edge(6,7,2)

dg3_mat = Graph(7, 'mat')
dg3_mat.add_edge(1,2,5)
dg3_mat.add_edge(1,3,6)
dg3_mat.add_edge(1,4,8)
dg3_mat.add_edge(1,5,2)
dg3_mat.add_edge(1,6,4)
dg3_mat.add_edge(1,7,4)
dg3_mat.add_edge(2,3,3)
dg3_mat.add_edge(2,4,2)
dg3_mat.add_edge(2,5,6)
dg3_mat.add_edge(2,6,1)
dg3_mat.add_edge(3,4,2)
dg3_mat.add_edge(3,5,8)
dg3_mat.add_edge(3,6,2)
dg3_mat.add_edge(3,7,7)
dg3_mat.add_edge(4,5,6)
dg3_mat.add_edge(4,6,9)
dg3_mat.add_edge(4,7,3)
dg3_mat.add_edge(5,6,9)
dg3_mat.add_edge(5,7,1)
dg3_mat.add_edge(6,7,2)


