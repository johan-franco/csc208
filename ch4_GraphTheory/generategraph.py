import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(5)

#pos = {0: (0, 0.5), 1: (1, 0.5), 2: (0.5, 1.5)}

#G.remove_edge(0, 1)
#G.remove_edge(1,2)
#G.remove_edge(0,2)
#abelmap = dict(zip(G.nodes(), ["R", "B", "G" ]))
colors = ["blue", "blue", "red", "red", "red", "blue","red","red","blue","blue"]

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color=colors, node_size=700, font_size=20)
plt.title('Graph with Edge (0, 1) Removed (Spanning Tree)')
plt.show()

