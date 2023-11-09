class GraphAdyMatrix:
    def __init__(self, num_of_nodes, directed):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)] for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        for row in range(len(self.m_adj_matrix)):
            print(self.m_adj_matrix[row])
       
        
        