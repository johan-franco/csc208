import matplotlib.pyplot as plt
import networkx as nx

def generate_k6_graph():
    G = nx.complete_graph(6)
    return G

def assign_specific_edge_colors(G):
    edge_colors = {
        ('A', 'B'): 'green',
        ('A', 'C'): 'green',
        ('A', 'D'): 'grey',
        ('A', 'E'): 'grey',
        ('A', 'V'): 'red',
        ('B', 'C'): 'green',
        ('B', 'D'): 'grey',
        ('B', 'E'): 'grey',
        ('B', 'V'): 'red',
        ('C', 'D'): 'grey',
        ('C', 'E'): 'grey',
        ('C', 'V'): 'red',
        ('D', 'E'): 'grey',
        ('D', 'V'): 'blue',
        ('E', 'V'): 'blue'
    }
    return edge_colors

def rename_nodes(G):
    mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'V'}
    G = nx.relabel_nodes(G, mapping)
    return G

def plot_graph_with_colors(G, edge_colors):
    pos = {
        'A': (0, 1), 'B': (0.87, 0.5), 'C': (0.87, -0.5),
        'D': (0, -1), 'V': (-0.87, -0.5), 'E': (-0.87, 0.5)
    }
    nx.draw(
        G, pos, with_labels=True, node_color='skyblue', node_size=1500,
        edge_color=[edge_colors[edge] for edge in G.edges()], width=2.0, font_size=10
    )
    
    plt.show()

if __name__ == "__main__":
    G = generate_k6_graph()
    G = rename_nodes(G) 
    edge_colors = assign_specific_edge_colors(G)
    plot_graph_with_colors(G, edge_colors)
