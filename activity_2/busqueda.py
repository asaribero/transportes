import heapq

# Estaciones congestionadas
congestionadas = ["C"]

def puede_moverse(grafo, origen, destino):
    return destino in grafo[origen]

def costo_extra(estacion):
    return 3 if estacion in congestionadas else 0

def heuristica(nodo, objetivo):
    # Heurística basada en letras (sencilla)
    return abs(ord(nodo[-1]) - ord(objetivo[-1]))

def a_estrella(grafo, inicio, objetivo):
    frontera = [(0, inicio, [])]
    visitados = set()

    while frontera:
        costo_actual, nodo_actual, camino = heapq.heappop(frontera)

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        camino = camino + [nodo_actual]

        if nodo_actual == objetivo:
            return camino, costo_actual

        for vecino in grafo[nodo_actual]:
            peso = grafo[nodo_actual][vecino]['weight'] + costo_extra(vecino)
            heur = heuristica(vecino, objetivo)
            heapq.heappush(frontera, (costo_actual + peso + heur, vecino, camino))

    return None, float('inf')
