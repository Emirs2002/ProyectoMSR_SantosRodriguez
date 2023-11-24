import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#GRAFICAR EL GRAFO CON SUS PESOS
def graficar_grafo(G, dijkstra_edges_javier):
    
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
    edges_dijks= get_dijkstra_edges(dijkstra_edges_javier)        
    nx.draw_networkx_edges(G,rotated_pos,edgelist=edges_dijks,width=4, edge_color="tab:red")

    #LABELS
    nx.draw_networkx_labels(G,rotated_pos,font_size=10)

    edge_labels = nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G,rotated_pos,edge_labels)
    
    # ax = plt.gca()
    # ax.margins(0.08)
    plt.tight_layout()
    plt.xlim(0,2)
    plt.ylim(0,2)
    plt.axis("off")
    plt.get_current_fig_manager().window.state('normal')
    plt.show()

 # guardar en una lista los arcos de dijkstra
def get_dijkstra_edges(dijkstra_lista):
    edges_dijks = []
    for i in range(len(dijkstra_lista)-1):
        edge_d = (dijkstra_lista[i],dijkstra_lista[i+1])
        edges_dijks.append(edge_d)

    return edges_dijks