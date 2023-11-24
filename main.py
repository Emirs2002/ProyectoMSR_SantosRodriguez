from GraphAdyMatrix import GraphAdyMatrix
from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
from utils import *

def main():
    
    # edges_list = [[0,1],[0,6],[1,7],[1,2],[2,3],[2,8],[3,4],[3,9],[4,5],[4,10],[5,11],[6,7],[6,12],[7,8],[7,13],
    #              [8,9],[8,14],[9,10],[9,15],[10,11],[10,16],[11,17],[12,13],[12,18],[13,14],[13,19],[14,15],[14,20],
    #              [15,16],[15,21],[16,17],[16,22],[17,23],[18,19],[18,24],[19,20],[19,25],[20,21],[20,26],[21,22],[21,27],[22,23],[22,28],
    #              [23,29],[24,25],[24,30],[25,26],[25,31],[26,27],[26,32],[27,28],[27,33],[28,29],[28,34],[29,35],[30,31],[31,32],[32,33],
    #              [33,34],[34,35]]
    
    edges_list_Javier = [[0,1,5],[0,6,5],[1,"Javier",7],[1,2,5],[2,3,5],[2,8,7],[3,4,5],[3,9,7],[4,5,5],[4,"Bar",5],[5,11,5],[6,"Javier",5],[6,12,5],["Javier",8,5],["Javier",13,7],
                  [8,9,5],[8,14,7],[9,"Bar",5],[9,15,7],["Bar",11,5],["Bar",16,5],[11,17,5],[12,13,5],[12,18,5],[13,14,5],[13,19,7],[14,15,5],[14,"Andreina",7],
                  [15,16,5],[15,21,7],[16,17,5],[16,22,5],[17,23,5],[18,19,5],[18,24,5],[19,"Andreina",5],[19,25,7],["Andreina",21,5],["Andreina",26,7],[21,22,5],[21,27,7],[22,23,5],[22,28,5],
                  [23,29,5],[24,25,10],[24,30,5],[25,26,10],[25,"Disco",7],[26,27,10],[26,32,7],[27,28,10],[27,"Cerveceria",7],[28,29,10],[28,34,5],[29,"Cafe",5],[30,"Disco",5],["Disco",32,5],[32,"Cerveceria",5],
                  ["Cerveceria",34,5],[34,"Cafe",5]]
    
    # print("")
    # print("GRAFO BELLO")
    G = Graph(edges_list_Javier).create_graph()

    # distance, path = find_shortest_path(G, "Javier","Bar")

    # print(distance)
    # print(path)

    
    grafo = GraphAdyMatrix(36)

    for edgePar in range(len(edges_list_Javier)):
        min_edge_list = edges_list_Javier[edgePar]
        grafo.add_edge(min_edge_list[0],min_edge_list[1],min_edge_list[2])


    print("")
    print("CON GRAFO A MANO")
    distance, path = grafo.dijkstra("Javier","Cerveceria")

    print(distance)
    print(path)


    graficar_grafo(G, list(path))

main()