
class GraphAdyMatrix:
    def __init__(self, num_of_nodes, edges_list):
        self.m_num_of_nodes = num_of_nodes
        self.node_labels = {} #diccionario donde se van a almacenar los vertices con sus labels
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)] for row in range(num_of_nodes)]
        
        for edgePar in range(len(edges_list)):
            min_edge_list = edges_list[edgePar]
            self.add_edge(min_edge_list[0],min_edge_list[1],min_edge_list[2])

    
    def add_edge(self, source, destination, weight):
        if source not in self.node_labels:
            self.node_labels[source] = len(self.node_labels)  # Asignar nuevo indice al nodo 1
        if destination not in self.node_labels:
            self.node_labels[destination] = len(self.node_labels)  # Asignar nuevo indice al nodo 2

        source_index = self.node_labels[source]
        destination_index = self.node_labels[destination]

        self.m_adj_matrix[source_index][destination_index] = weight
        self.m_adj_matrix[destination_index][source_index] = weight 
    
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
        distance = {node: float('inf') for node in self.node_labels} #todos los valores a infinito
        distance[source] = 0 #distancia del origen se inicializa en 0
        visited = set()  # set para guardar los nodos visitados
        
        # Mantiene el camino hacia el nodo destino. 
        # Cada camino es una lista vacia al inicio
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

            visited.add(current_node)

            # actualizar las distancias de los nodos vecinos
            row=self.m_adj_matrix[self.node_labels[current_node]]
            for neighbor, weight in enumerate(row): #itera sobre los vecinos, sobre la fila de la matriz donde esta el current node
                if weight > 0:
                    new_distance = distance[current_node] + weight #se suma a la distancia acumulada
                    
                    neighbor_pos = list(self.node_labels.keys())[neighbor]#hace una lista con las llaves del diccionario y busca en la posicion del vecino
                   
                    if new_distance < distance[neighbor_pos]: #este mismo sera el indice en el diccionario distance
                                                                                        
                        distance[neighbor_pos] = new_distance #se actualiza la nueva distancia para el neighbor en el dic de distancias
                        path[neighbor_pos] = path[current_node] + [current_node] #en el dict path se guarda el camino anterior mas el nodo actual

        shortest_distance = distance[destination]
        shortest_path = path[destination] + [destination]

        return shortest_distance, shortest_path
       