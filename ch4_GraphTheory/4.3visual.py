import networkx as nx
import matplotlib.pyplot as plt

B = nx.Graph()

males = ['M1', 'M2', 'M3', 'M4', 'M5']
females = ['F1', 'F2', 'F3', 'F4', 'F5']

B.add_nodes_from(males, bipartite=0)
B.add_nodes_from(females, bipartite=1)

relationships = [('M1', 'F1'), ('M1', 'F2'), ('M2', 'F2'), ('M2', 'F3'),
                 ('M3', 'F3'), ('M3', 'F4'), ('M4', 'F4'), ('M4', 'F5'),
                 ('M5', 'F1'), ('M5', 'F5')]

B.add_edges_from(relationships)

pos = {}
pos.update((node, (1, index)) for index, node in enumerate(males))  
pos.update((node, (2, index)) for index, node in enumerate(females)) 


plt.figure(figsize=(8, 6))
nx.draw(B, pos, with_labels=True, node_color=['skyblue' if node in males else 'lightgreen' for node in B.nodes()],
        node_size=3000, font_size=16, font_color='black', edge_color='gray')
plt.title("Bipartite Graph of Friends and Their Relationships")
plt.show()



