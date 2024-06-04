import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(4)




plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  

#G.remove_edge(0,2)
colors = ['green', 'blue', 'red', 'orange']

# Assign colors to nodes
node_colors = [colors for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=3000, font_size=16, font_color='black', edge_color='gray')
plt.title("Example of Brook's Theoreom")
plt.show()



