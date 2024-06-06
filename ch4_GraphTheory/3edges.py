import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5, 6])

G.add_edges_from([(1, 2), (1, 3), (1, 4), (5, 1), (1,6) ])  # Cycle 1


plt.figure(figsize=(8, 6)) 
nx.draw(G, with_labels=True, node_color= "skyblue", edge_color=["blue", "red", "blue", "red","green"], node_size=700, font_size=20)
plt.title('Graph with Multiple Cycles')
plt.show()
