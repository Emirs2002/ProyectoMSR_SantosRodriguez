from GraphNx import GraphNx
from utils import *

def main():
    
    edges_list_Javier = [[0,1,5],[0,6,5],[1,"Javier",7],[1,2,5],[2,3,5],[2,8,7],[3,4,5],[3,9,7],[4,5,5],[4,"Bar",5],[5,11,5],[6,"Javier",5],[6,12,5],["Javier",8,5],["Javier",13,7],
                  [8,9,5],[8,14,7],[9,"Bar",5],[9,15,7],["Bar",11,5],["Bar",16,5],[11,17,5],[12,13,5],[12,18,5],[13,14,5],[13,19,7],[14,15,5],[14,"Andreina",7],
                  [15,16,5],[15,21,7],[16,17,5],[16,22,5],[17,23,5],[18,19,5],[18,24,5],[19,"Andreina",5],[19,25,7],["Andreina",21,5],["Andreina",26,7],[21,22,5],[21,27,7],[22,23,5],[22,28,5],
                  [23,29,5],[24,25,10],[24,30,5],[25,26,10],[25,"Disco",7],[26,27,10],[26,32,7],[27,28,10],[27,"Cerveceria",7],[28,29,10],[28,34,5],[29,"Cafe",5],[30,"Disco",5],["Disco",32,5],[32,"Cerveceria",5],
                  ["Cerveceria",34,5],[34,"Cafe",5]]

     # Grafo networkx
    G = GraphNx(edges_list_Javier).create_graph()
    
    #path_javier, path_andreina, late, time, distance_andreina, distance_javier = run_graphs(edges_list_Javier, "Cafe")

    #print(f"Andreina tarda: {distance_andreina}")
    #print(f"Javier tarda: {distance_javier}")
    #print("")
    #print("Llega tarde: " + late)
    #print(f"Deberia salir:{time} min antes")

    #gui
    gui(G,  edges_list_Javier)


main()