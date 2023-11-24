import networkx as nx
import matplotlib.pyplot as plt

#GRAFICAR EL GRAFO CON SUS PESOS
def graficar_grafo(G):

    pos = nx.spring_layout(G, seed = 7)

    #draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=900, node_color="tab:blue")
    nx.draw_networkx_nodes(G, pos, node_size=900, nodelist=["Javier"], node_color="tab:orange")
    nx.draw_networkx_nodes(G, pos, node_size=900, nodelist=["Andreina"], node_color="tab:pink")

    nx.draw_networkx_nodes(G, pos, node_size=900, nodelist=["Bar"], node_color="tab:red")
    nx.draw_networkx_nodes(G, pos, node_size=900, nodelist=["Cafe"], node_color="whitesmoke")
    nx.draw_networkx_nodes(G, pos, node_size=900, nodelist=["Disco"], node_color="tab:purple")
    nx.draw_networkx_nodes(G, pos, node_size=900, nodelist=["Cerveceria"], node_color="yellow")

    #draw edges
    elist = [(u,v) for (u,v,d) in G.edges(data = True)]
    nx.draw_networkx_edges(G,pos,edgelist=elist,width=3)

    #LABELS
    nx.draw_networkx_labels(G,pos,font_size=9)

    edge_labels = nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G,pos,edge_labels)
    
    ax = plt.gca()
    ax.margins(0.08)
    plt.tight_layout()
    plt.axis("off")
    plt.show()
