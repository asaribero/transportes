import networkx as nx
import matplotlib.pyplot as plt

def mostrar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    etiquetas = nx.get_edge_attributes(grafo, 'weight')
    
    nx.draw(grafo, pos, with_labels=True, node_color='skyblue', node_size=2000)
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=etiquetas)
    plt.title("Mapa del Sistema de Transporte")
    plt.savefig("resultados.png")
    plt.show()
