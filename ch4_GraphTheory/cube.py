import networkx as nx
import matplotlib.pyplot as plt

B = nx.Graph()

groupa = ['B1', 'B2', 'B3', 'B4']
groupb = ['R1', 'R2', 'R3', 'R4']

B.add_nodes_from(groupa, bipartite=0)
B.add_nodes_from(groupb, bipartite=1)

relationships = [('R1', 'B1'), ('R1', 'B2'), ('R1', 'B4'), ('B1', 'R4'),
                 ('B1', 'R2'), ('B2', 'R2'), ('B2', 'R3'), ('R2', 'B3'),
                 ('R3', 'B4'), ('R3', 'B3'), ('B3', 'R4'), ('B4','R4')]

B.add_edges_from(relationships)



pos = {"R1": (-1, 1), "B1": (1, 1), "R2": (.5, .5), "B2": (-.5, .5), "R3": (-.5, -.5), "B3": (.5,-.5), "B4": (-1,-1), "R4":(1,-1)}



plt.figure(figsize=(8, 6))
nx.draw(B, pos, with_labels=True, node_color=['skyblue' if node in groupb else 'lightgreen' for node in B.nodes()],
        node_size=3000, font_size=16, font_color='black', edge_color='gray')
plt.title("Bipartite Graph of Friends and Their Relationships")
plt.show()



