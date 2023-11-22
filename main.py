from GraphAdyMatrix import GraphAdyMatrix
import networkx as nx
import matplotlib.pyplot as plt

def main():
    grafo = GraphAdyMatrix(36,False)

    G = nx.Graph()
    
    vertex_list = [["0",False],["1",False],["2",False],["3",False],["4",False],["5",False],["6",False],["Javier",False],["8",False],["9",False],
                   ["Bar",True],["11",False],["12",False],["13", False],["14",False],["15",False],["16",False],["17", False],["18", False],
                   ["19", False],["Andreina", False],["21", False],["22", False],["23", False],["24", False],["25", False],["26", False],
                   ["27", False],["28", False],["29", False],["30", False],["Disco", True],["32", False],["Cerveceria", True],["34", False],
                   ["Cafe", True]]
    edges_list = [[0,1],[0,6],[1,7],[1,2],[2,3],[2,8],[3,4],[3,9],[4,5],[4,10],[5,11],[6,7],[6,12],[7,8],[7,13],
                  [8,9],[8,14],[9,10],[9,15],[10,11],[10,16],[11,17],[12,13],[12,18],[13,14],[13,19],[14,15],[14,20],
                  [15,16],[15,21],[16,17],[16,22],[17,23],[18,19],[18,24],[19,20],[19,25],[20,21],[20,26],[21,22],[21,27],[22,23],[22,28],
                  [23,29],[24,25],[24,30],[25,26],[25,31],[26,27],[26,32],[27,28],[27,33],[28,29],[28,34],[29,35],[30,31],[31,32],[32,33],
                  [33,34],[34,35]]
    
   
    # for vertex in range(len(vertex_list)):
    #     min_vertex_list = vertex_list[vertex]
    #     grafo.create_vertex(min_vertex_list[0],min_vertex_list[1])
        

    for edgePar in range(len(edges_list)):
        min_edge_list = edges_list[edgePar]
        #grafo.add_edge(min_edge_list[0],min_edge_list[1])
        G.add_nodes_from(min_edge_list)
        G.add_edge(min_edge_list[0],min_edge_list[1])
    
    nx.draw(G,with_labels=True)
    plt.show()


    # grafo.print_adj_matrix()
    # print("")
    # print(f"VERTICES {len(grafo.vertexList)}")
    # for ver in range(len(grafo.vertexList)):
    #     print(grafo.vertexList[ver].name)


main()