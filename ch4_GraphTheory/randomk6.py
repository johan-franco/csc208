
import matplotlib.pyplot as plt
import networkx as nx
import random

def generate_k6_graph():
    G = nx.complete_graph(6)
    return G

def randomize_edge_colors(G):
    edges = list(G.edges())
    random.shuffle(edges)
    
    num_edges = len(edges)
    half_edges = num_edges // 2
    
    red_edges = edges[:half_edges]
    blue_edges = edges[half_edges:]
    
    edge_colors = {}
    for edge in red_edges:
        edge_colors[edge] = 'red'
    for edge in blue_edges:
        edge_colors[edge] = 'blue'
        
    return edge_colors

def plot_graph_with_colors(G, edge_colors):
    pos = {0: (0, 1), 1: (0.5, 0.75), 2: (0.5, 0.25), 3: (0, 0), 4: (-0.5, 0.25), 5: (-0.5, 0.75)}
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color=[edge_colors[edge] for edge in G.edges()], width=2.0, font_size=10)
    plt.show()


G = generate_k6_graph()
edge_colors = randomize_edge_colors(G)
plot_graph_with_colors(G, edge_colors)
