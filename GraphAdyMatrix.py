from Vertex import Vertex
class GraphAdyMatrix:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.node_labels = {} #diccionario donde se van a almacenar los vertices con sus labels
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)] for row in range(num_of_nodes)]
        

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def add_edge(self, source, destination, weight):
        if source not in self.node_labels:
            self.node_labels[source] = len(self.node_labels)  # Assign a new index for the source node
        if destination not in self.node_labels:
            self.node_labels[destination] = len(self.node_labels)  # Assign a new index for the destination node

        source_index = self.node_labels[source]
        destination_index = self.node_labels[destination]

        self.m_adj_matrix[source_index][destination_index] = weight
        self.m_adj_matrix[destination_index][source_index] = weight  # Assuming the graph is undirected
    
    def remove_edge(self, node1,node2):

        source_index = self.node_labels[node1]
        destination_index = self.node_labels[node2]

        self.m_adj_matrix[source_index][destination_index]=0
        self.m_adj_matrix[destination_index][source_index]=0


    def print_adj_matrix(self):
        for row in range(len(self.m_adj_matrix)):
            print(self.m_adj_matrix[row])

    def dijkstra(self, source, destination):
        # Inicializacion
        distance = {node: float('inf') for node in self.node_labels}
        distance[source] = 0

        # set de visitados
        visited = set()

        # Mantiene el camino hacia el nodo destino. Cada camino es una lista vacia al inicio
        path = {node: [] for node in self.node_labels}

        while len(visited) < len(self.node_labels):
            # Encontrar el nodo con la minima distancia 
            unvisited_nodes = [node for node in distance if node not in visited] #lista de nodos que no estan es visitados
            min_distance = float('inf')
            current_node = None

            for node in unvisited_nodes:
                if distance[node] < min_distance: 
                    min_distance = distance[node]
                    current_node = node

            #current_node = min((node for node in distance if node not in visited), key=lambda x: distance[x])
            visited.add(current_node)

            # actualizar las distancias de los nodos vecinos
            for neighbor, weight in enumerate(self.m_adj_matrix[self.node_labels[current_node]]): #itera sobre los vecinos, sobre la fila de la matriz donde esta el current node
                if weight > 0:
                    new_distance = distance[current_node] + weight
                    if new_distance < distance[list(self.node_labels.keys())[neighbor]]:
                        distance[list(self.node_labels.keys())[neighbor]] = new_distance
                        path[list(self.node_labels.keys())[neighbor]] = path[current_node] + [current_node]

        shortest_distance = distance[destination]
        shortest_path = path[destination] + [destination]

        return shortest_distance, shortest_path
       
   