from GraphAdyMatrix import GraphAdyMatrix
from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

def main():
    grafo = GraphAdyMatrix(36,False)
    #edges_list = [[0,1],[0,6],[1,7],[1,2],[2,3],[2,8],[3,4],[3,9],[4,5],[4,10],[5,11],[6,7],[6,12],[7,8],[7,13],
     #             [8,9],[8,14],[9,10],[9,15],[10,11],[10,16],[11,17],[12,13],[12,18],[13,14],[13,19],[14,15],[14,20],
      #            [15,16],[15,21],[16,17],[16,22],[17,23],[18,19],[18,24],[19,20],[19,25],[20,21],[20,26],[21,22],[21,27],[22,23],[22,28],
       #           [23,29],[24,25],[24,30],[25,26],[25,31],[26,27],[26,32],[27,28],[27,33],[28,29],[28,34],[29,35],[30,31],[31,32],[32,33],
        #          [33,34],[34,35]]
    
   
    
   # vertex_list = [["0",False],["1",False],["2",False],["3",False],["4",False],["5",False],["6",False],["Javier",False],["8",False],["9",False],
   #                ["Bar",True],["11",False],["12",False],["13", False],["14",False],["15",False],["16",False],["17", False],["18", False],
   #                ["19", False],["Andreina", False],["21", False],["22", False],["23", False],["24", False],["25", False],["26", False],
   #                ["27", False],["28", False],["29", False],["30", False],["Disco", True],["32", False],["Cerveceria", True],["34", False],
   #                ["Cafe", True]]
    edges_list_Javier = [[0,1, 5],[0,6,5],[1,7,7],[1,2,5],[2,3,5],[2,8,7],[3,4,5],[3,9,7],[4,5,5],[4,10,5],[5,11,5],[6,7,5],[6,12,5],[7,8,5],[7,13,7],
                  [8,9,5],[8,14,7],[9,10,5],[9,15,7],[10,11,5],[10,16,5],[11,17,5],[12,13,5],[12,18,5],[13,14,5],[13,19,7],[14,15,5],[14,20,7],
                  [15,16,5],[15,21,7],[16,17,5],[16,22,5],[17,23,5],[18,19,5],[18,24,5],[19,20,5],[19,25,7],[20,21,5],[20,26,7],[21,22,5],[21,27,7],[22,23,5],[22,28,5],
                  [23,29,5],[24,25,10],[24,30,5],[25,26,10],[25,31,7],[26,27,10],[26,32,7],[27,28,10],[27,33,7],[28,29,10],[28,34,5],[29,35,5],[30,31,5],[31,32,5],[32,33,5],
                  [33,34,5],[34,35,5]]
    
    G = Graph(edges_list_Javier).create_graph()


    #GRAFICAR EL GRAFO CON SUS PESOS
    
    pos = nx.spring_layout(G, seed=7)

    #draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    #draw edges
    elist = [(u,v) for (u,v,d) in G.edges(data = True)]
    nx.draw_networkx_edges(G,pos,edgelist=elist,width=5)

    #LABELS
    nx.draw_networkx_labels(G,pos,font_size=14)

    edge_labels = nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G,pos,edge_labels)
    
    
    plt.axis("off")
    plt.tight_layout()
    plt.show()



    #nx.draw(G,with_labels=True)
    #plt.show()


main()