import networkx as nx
import matplotlib.pyplot as plt
from GraphAdyMatrix import GraphAdyMatrix
from GraphNx import GraphNx

def initialize_graphs(edges, destination):

    #Grafo Javier
    grafo_Javier = GraphAdyMatrix(36,edges)

    #dijkstra Javier
    distance_javier, path_javier = grafo_Javier.dijkstra("Javier",destination)
    
    print("JAVIER")
    print(distance_javier)
    print(path_javier)
    

    #crear grafo de andreina
    #lista de arcos con los pesos de andreina (2 + pesosJavier)
    edges_list_Andreina = [[u,v,w+2] for [u,v,w] in edges]

    #se hace un nuevo grafo con estos pesos
    grafo_andreina = GraphAdyMatrix(36,edges_list_Andreina)
    
    #borrar los arcos por los que paso javier tras el dijkstra
    new_grafo_andreina = erase_visited_edges(grafo_andreina, list(path_javier))
    
    
    #dijkstra Andreina
    distance_andreina, path_andreina = new_grafo_andreina.dijkstra("Andreina",destination)

    print("")
    print("ANDREINA")
    print(distance_andreina)
    print(path_andreina)

    return distance_javier, distance_andreina, path_javier, path_andreina

    

#GRAFICAR EL GRAFO CON SUS PESOS
def graficar_grafo(G, dijkstra_edges_javier,dijkstra_edges_Andreina):
    
    pos = nx.spring_layout(G, seed = 7)

    rotated_pos = {node: (y, -x) for node, (x, y) in pos.items()}

    #pintar los nodos
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, node_color="tab:blue")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Javier"], node_color="tab:orange")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Andreina"], node_color="tab:pink")

    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Bar"], node_color="tab:red")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Cafe"], node_color="whitesmoke")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Disco"], node_color="tab:purple")
    nx.draw_networkx_nodes(G, rotated_pos, node_size=900, nodelist=["Cerveceria"], node_color="yellow")

    #pintar arcos
    elist = [(u,v) for (u,v,d) in G.edges(data = True)]
    nx.draw_networkx_edges(G,rotated_pos,edgelist=elist,width=3)

    #pintar los arcos de dijkstra
    edges_dijks_jav= get_dijkstra_edges(dijkstra_edges_javier)        
    edges_dijks_and= get_dijkstra_edges(dijkstra_edges_Andreina)        
    nx.draw_networkx_edges(G,rotated_pos,edgelist=edges_dijks_jav,width=4, edge_color="orange")
    nx.draw_networkx_edges(G,rotated_pos,edgelist=edges_dijks_and,width=4, edge_color="pink")

    #LABELS
    nx.draw_networkx_labels(G,rotated_pos,font_size=10)

    # edge_labels = nx.get_edge_attributes(G,"weight")
    # nx.draw_networkx_edge_labels(G,rotated_pos,edge_labels)
    

    plt.tight_layout()
    plt.xlim(0,2)
    plt.ylim(0,2)
    plt.axis("off")
    plt.show()

 # guardar en una lista los arcos de dijkstra
def get_dijkstra_edges(dijkstra_lista):
    edges_dijks = []
    for i in range(len(dijkstra_lista)-1):
        edge_d = (dijkstra_lista[i],dijkstra_lista[i+1])
        edges_dijks.append(edge_d)

    return edges_dijks

#borrar arcos para el segundo recorrido
def erase_visited_edges(grafo, dijkstra_lista):
    grafo_nuevo = grafo
    edges_dijks = get_dijkstra_edges(dijkstra_lista)

    for edge in range(len(edges_dijks)):
        min_edge_list = list(edges_dijks[edge])
        grafo_nuevo.remove_edge(min_edge_list[0],min_edge_list[1])
    
    return grafo_nuevo 