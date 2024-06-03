
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5])

G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])  # Cycle 1
G.add_edges_from([(1, 5), (5, 4)])                 # Cycle 2
G.add_edges_from([(2, 5)])                        
G.remove_eedge(2,5)

#G.remove_edge(4,1) (removing this specific edge is not working for whatever reason)
#G.remove_edge(3,4)
#G.remove_edge(2,3)

pos = {1: (0.5, 0), 2: (0.25, 1), 3: (0.75, 1), 4: (1, 0), 5: (0, 0)}

plt.figure(figsize=(8, 6)) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=20)
plt.title('Graph with Multiple Cycles')
plt.show()
