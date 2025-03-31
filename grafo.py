import networkx as nx

def crear_grafo():
    grafo = nx.DiGraph()
    grafo.add_edge("A", "B", weight=2)
    grafo.add_edge("A", "C", weight=4)
    grafo.add_edge("B", "D", weight=7)
    grafo.add_edge("C", "D", weight=1)
    grafo.add_edge("C", "E", weight=3)
    grafo.add_edge("D", "F", weight=1)
    grafo.add_edge("E", "F", weight=5)
    return grafo