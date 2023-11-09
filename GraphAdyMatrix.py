from Vertex import Vertex
class GraphAdyMatrix:
    def __init__(self, num_of_nodes, directed):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)] for row in range(num_of_nodes)]
        self.size = 0
        self.vertexList = []

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def add_edge(self, node1, node2, weight=1):
        exists = self.edge_exists(node1,node2)

        if node1 != node2 and not exists:
            self.m_adj_matrix[node1][node2] = weight

            if not self.m_directed:
                self.m_adj_matrix[node2][node1] = weight

    def edge_exists(self,node1,node2):
        exists = False
        if self.m_adj_matrix[node1][node2] != 0:
            exists = True
        
        return exists
    
    def remove_edge(self, node1,node2):
        if self.m_adj_matrix[node1][node2] == 0:
            print("no existe la arista")
        else:
            self.m_adj_matrix[node1][node2]=0
            self.m_adj_matrix[node2][node1]=0

    def create_vertex(self,nom,is_couple):
        verti = Vertex(nom,self.size,is_couple)
        self.vertexList.append(verti)
        self.size += 1

    def search_index(self,nom):
        
        exists = False
        i = 0
        while i < self.size and not exists:
            if nom == self.vertexList[i].name:
                exists = True 
            else:
                 i += 1;
        
        if exists:
            return i
        else:
            return -1 

    def print_adj_matrix(self):
        for row in range(len(self.m_adj_matrix)):
            print(self.m_adj_matrix[row])
       
   