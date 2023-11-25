from cgitb import text
import networkx as nx
import matplotlib.pyplot as plt
from GraphAdyMatrix import GraphAdyMatrix
from GraphNx import GraphNx

def run_graphs(edges, destination):

    #Grafo Javier
    grafo_Javier = GraphAdyMatrix(36,edges)

    #dijkstra Javier
    distance_javier, path_javier = grafo_Javier.dijkstra("Javier",destination)
    

    #crear grafo de andreina
    #lista de arcos con los pesos de andreina (2 + pesosJavier)
    edges_list_Andreina = [[u,v,w+2] for [u,v,w] in edges]

    #se hace un nuevo grafo con estos pesos
    grafo_andreina = GraphAdyMatrix(36,edges_list_Andreina)
    
    #borrar los arcos por los que paso javier tras el dijkstra
    new_grafo_andreina = erase_visited_edges(grafo_andreina, list(path_javier))
    
    
    #dijkstra Andreina
    distance_andreina, path_andreina = new_grafo_andreina.dijkstra("Andreina",destination)

    late, time = calculate_time(distance_andreina, distance_javier)

    return path_javier, path_andreina, late, time, distance_andreina, distance_javier

def calculate_time(dis_and, dis_jav):
    late = ""
    time = 0

    if dis_jav > dis_and:
        late = "Javier"
        time = dis_jav - dis_and
    elif dis_and > dis_jav:
        late = "Andreina"
        time = dis_and - dis_jav

    return late, time

import customtkinter as ctk
import tkinter as tk


#GRAFICAR EL GRAFO CON CAMINOS
def graficar_grafo_paths(G, dijkstra_edges_javier,dijkstra_edges_Andreina):
    
    if dijkstra_edges_javier == [] and dijkstra_edges_Andreina == []:
        graficar_grafo(G)
    else:
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


        plt.tight_layout()
        plt.xlim(0,2)
        plt.ylim(0,2)
        plt.axis("off")
        plt.show()

#Graficar grafo general
def graficar_grafo(G):
    
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


    #LABELS
    nx.draw_networkx_labels(G,rotated_pos,font_size=10)


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


def gui(G, edges):

    #Variables y fucniones auxiliares
    def combobox_callback(choice):
        print(choice)
    
    options = ["", "Bar", "Cerveceria", "Disco", "Cafe"]

    path_javier = []
    path_andreina = []
    late = ""
    time = 0
    distance_andreina = 0
    distance_javier = 0

    def calcular_todo(edges, option, entry1A, entry1J, entry2A, entry2J):
        if option != "":
            path_javier, path_andreina, late, time, distance_andreina, distance_javier = run_graphs(edges, option)
            entry1A.configure(text=str(distance_andreina))
            entry1J.configure(text=str(distance_javier))
            if late == "Andreina":
                entry2J.configure(text="0")   
                entry2A.configure(text=str(time))  
            else:
                entry2A.configure(text="0") 
                entry2J.configure(text=str(time)) 
            graficar_grafo_paths(G, list(path_javier),list(path_andreina))      



    #setup interaz
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    root = ctk.CTk()
    root.geometry("500x400")
    root.title("ProyectoMSR")


    #Frames y labels
    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    titulo = ctk.CTkLabel(master=frame, text="Amor prohibido en las calles de Bogota", font=("Arial Black", 16))
    titulo.pack(pady=10)
    grafo_info = ctk.CTkFrame(master=frame)
    grafo_info.pack(padx=10, pady=10, fill="both")
    label1 = ctk.CTkLabel(master=grafo_info,  text="Destino", font=("Arial Black", 14))
    label1.pack(pady=10, padx=10)

    #opciones para generar el camino
    selected_option = tk.StringVar()
    selected_option.set(options[0])
    combobox = ctk.CTkComboBox(grafo_info, values=options, variable=selected_option, command=combobox_callback)
    combobox.pack(pady=10, padx=10)

    #buton para calcular dijkstra
    ir_button=ctk.CTkButton(grafo_info, text="Ir", command=lambda: calcular_todo(edges, selected_option.get(), entry1_andreina, entry1_javier, entry2_andreina, entry2_javier))
    ir_button.pack(padx=10, pady=10, anchor="e")
   
    #Resultados del recorrido
    resultados_info = ctk.CTkFrame(master=frame)
    resultados_info.pack(padx=10, pady=10, fill="both")
    resultados_info.columnconfigure(0, weight=1)
    resultados_info.columnconfigure(1, weight=1)
    resultados_andreina = ctk.CTkLabel(master=resultados_info, text="Andreina", font=("Arial Black", 14))
    resultados_javier = ctk.CTkLabel(master=resultados_info, text="Javier", font=("Arial Black", 14))
    duracion_andreina = ctk.CTkLabel(master=resultados_info, text="Duracion total: ", font=("Arial Black", 10))
    entry1_andreina = ctk.CTkLabel(master=resultados_info, width=80, text=str(distance_andreina))
    duracion_javier = ctk.CTkLabel(master=resultados_info, text="Duracion total: ", font=("Arial Black", 10))
    entry1_javier = ctk.CTkLabel(master=resultados_info, width=80, text=str(distance_javier))
    antes_andreina = ctk.CTkLabel(master=resultados_info, text="Sale antes por: ", font=("Arial Black", 10))
    entry2_andreina = ctk.CTkLabel(master=resultados_info, width=80, text=str(time))
    antes_javier = ctk.CTkLabel(master=resultados_info, text="Sale antes por: ", font=("Arial Black", 10))
    entry2_javier = ctk.CTkLabel(master=resultados_info, width=80, text=str(time))


    resultados_andreina.grid(row=0,column=0, padx=10, pady=10, sticky="we")
    resultados_javier.grid(row=0, column=1,  padx=10, pady=10, sticky="we")
    duracion_andreina.grid(row=1, column=0, sticky="w", padx=10)
    entry1_andreina.grid(row=1, column=0, padx=10, sticky="e")
    duracion_javier.grid(row=1, column=1, sticky="w", padx=10)
    entry1_javier.grid(row=1, column=1, padx=10, sticky="e")
    antes_andreina.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    entry2_andreina.grid(row=2, column=0, padx=10, sticky="e", pady=10)
    antes_javier.grid(row=2, column=1, sticky="w", padx=10, pady=10)
    entry2_javier.grid(row=2, column=1, padx=10, sticky="e", pady=10)
   

    root.mainloop()
