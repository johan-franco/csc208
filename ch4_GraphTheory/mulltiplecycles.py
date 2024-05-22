
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph with multiple cycles
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges forming cycles
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])  # Cycle 1
G.add_edges_from([(1, 5), (5, 4)])                 # Cycle 2
G.add_edges_from([(2, 5)])                         # Additional edge

# Define positions for the nodes
pos = {1: (0.5, 0), 2: (0.25, 1), 3: (0.75, 1), 4: (1, 0), 5: (0, 0)}

# Visualize the graph with the fixed positions
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=20)
plt.title('Graph with Multiple Cycles')
plt.show()
