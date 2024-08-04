#create and visualize random graph

import networkx as nx
import matplotlib.pyplot as plt
import random

def create_random_graph(n, p):
    G = nx.DiGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                G.add_edge(i, j)
    return G

def visualize_graph(G):
    nx.draw(G, with_labels=False, node_size=40, node_color='blue', edge_color='gray')
    plt.show()

G = create_random_graph(50, 0.2)
visualize_graph(G)