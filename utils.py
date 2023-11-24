import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#GRAFICAR EL GRAFO CON SUS PESOS
def graficar_grafo(G, dijkstra_edges):
    
    pos = nx.spring_layout(G, seed = 7)

    rotated_pos = {node: (y, -x) for node, (x, y) in pos.items()}

    #draw nodes
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, node_color="tab:blue")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Javier"], node_color="tab:orange")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Andreina"], node_color="tab:pink")

    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Bar"], node_color="tab:red")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Cafe"], node_color="whitesmoke")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Disco"], node_color="tab:purple")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Cerveceria"], node_color="yellow")

    #draw edges
    elist = [(u,v) for (u,v,d) in G.edges(data = True)]
    nx.draw_networkx_edges(G,rotated_pos,edgelist=elist,width=3)

    # guardar en una lista los arcos de dijkstra
    edges_dijks = []
    for i in range(len(dijkstra_edges)-1):
        edge_d = (dijkstra_edges[i],dijkstra_edges[i+1])
        edges_dijks.append(edge_d)

    #pintar los arcos de dijkstra
    nx.draw_networkx_edges(G,rotated_pos,edgelist=edges_dijks,width=3, edge_color="tab:red")

    #LABELS
    nx.draw_networkx_labels(G,rotated_pos,font_size=9)

    edge_labels = nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G,rotated_pos,edge_labels)
    
    # ax = plt.gca()
    # ax.margins(0.08)
    plt.tight_layout()
    plt.xlim(0,1.60)
    plt.ylim(0,1.60)
    plt.axis("off")
    plt.get_current_fig_manager().window.state('normal')
    plt.show()

def find_shortest_path(graph, source, destination):
    # Inicializacion
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0

    # Create a dictionary to store the previous node in the shortest path
    previous = {node: None for node in graph.nodes()}

    # Create a set to store the visited nodes
    visited = set()

    # Iterate until all nodes have been visited
    while len(visited) < graph.number_of_nodes():
        # Find the node with the minimum distance that has not been visited
        min_distance = float('inf')
        min_node = None
        for node in graph.nodes():
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        # If the minimum node is the destination, stop the algorithm
        if min_node == destination:
            break

        # Mark the minimum node as visited
        visited.add(min_node)

        # Update the distances to the neighbors of the minimum node
        for neighbor in graph.neighbors(min_node):
            distance = distances[min_node] + graph[min_node][neighbor]['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = min_node

    # Build the shortest path from the source to the destination
    path = []
    node = destination
    while node is not None:
        path.insert(0, node)
        node = previous[node]

    return distances[destination], path