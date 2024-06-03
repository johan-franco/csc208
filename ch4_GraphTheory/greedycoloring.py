import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

friends = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
G.add_nodes_from(friends)

conflicts = [('A', 'C'), ('A', 'F'), ('A', 'J'),
             ('B', 'J'),
             ('C', 'A'), ('C', 'E'), ('C', 'F'),
             ('D', 'H'),
             ('E', 'C'), ('E', 'F'), ('E', 'G'),
             ('F', 'A'), ('F', 'C'), ('F', 'E'), ('F', 'G'), ('F', 'I'),
             ('G', 'E'), ('G', 'F'), ('G', 'I'),
             ('H', 'D'),
             ('I', 'A'), ('I', 'F'), ('I', 'G'),
             ('J', 'B')]

G.add_edges_from(conflicts)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  

# Find the chromatic number 
coloring = nx.coloring.greedy_color(G, strategy="largest_first")

colors = ['red', 'blue', 'green', 'orange']

# Assign colors to nodes
node_colors = [colors[coloring[node]] for node in G.nodes()]

nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=16, font_color='black', edge_color='gray')
plt.title("Graph of Friends and Their Conflicts with Car Assignments")
plt.show()

print(f"Coloring of the graph: {coloring}")


