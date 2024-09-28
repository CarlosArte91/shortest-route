import networkx as nx
import matplotlib.pyplot as plt

"""
En el siguiente ejercicio se crea un grafo dirigido con 11 nodos, donde cada
nodo representa una estación del transporte público.
Con la ayuda de la librería networkx se establecerá la ruta más corta para ir
de la estación inicial 'I' a la estación final 'F'
"""

# Creación del grafo
grafo = nx.DiGraph()

"""
Creación de un arreglo con los diferentes nodos que representan las estaciones
y la distancia que hay entre una estación y otra.
"""
estaciones = [
    ("I", "B", 3.0), ("I", "E", 2.0),
    ("B", "C", 5.0),
    ("C", "D", 2.0), ("C", "G", 1.0),
    ("D", "E", 3.0),
    ("E", "H", 3.0),
    ("H", "G", 10.0), ("H", "A", 4.0),
    ("A", "F", 1.0), ("A", "K", 5.0),
    ("F", "K", 3.0),
    ("G", "J", 2.0),
    ("J", "K", 1.0), ("J", "F", 2.0),
]

# Se añaden las estaciones (aristas) al grafo.
grafo.add_weighted_edges_from(estaciones)

# Función para visualizar el grafo usando la librería matplotlib
def draw_graph(graph, route, color):
    # Posiciones de los nodos
    pos = {
        "I": (0, 6),
        "B": (2, 14),
        "E": (6, 8),
        "C": (7, 22),
        "D": (8, 15),
        "G": (12, 20),
        "H": (8, 1),
        "A": (14, 5),
        "F": (14, 11),
        "J": (18, 17),
        "K": (21, 12),
    }

    # Colores para los nodos
    color_map = []
    for node in graph.nodes():
        if node in route:
            color_map.append(color)
        else:
            color_map.append('#bae6fd')

    labels = nx.get_edge_attributes(graph, 'weight')  # Pesos de las aristas
    nx.draw(graph, pos, with_labels=True, node_color=color_map, node_size=1500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

# Visualización del grafo
draw_graph(grafo, ['I', 'F'], '#22c55e')

try:
    shortest_route = nx.dijkstra_path(grafo, source="I", target="F")

    # Mostrar la ruta más corta
    print(f"Ruta más corta: {shortest_route}")
    draw_graph(grafo, shortest_route, '#c084fc')

except nx.NetworkXNoPath:
    print("No se encontró una ruta entre los nodos especificados.")
