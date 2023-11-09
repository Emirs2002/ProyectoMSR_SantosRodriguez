from GraphAdyMatrix import GraphAdyMatrix

def main():
    grafo = GraphAdyMatrix(36,False)

    grafo.add_edge(0,1)
    grafo.add_edge(0,6)
    grafo.add_edge(1,7)
    grafo.add_edge(1,2)
    grafo.add_edge(2,3)
    grafo.add_edge(2,8)
    

    grafo.print_adj_matrix()


main()