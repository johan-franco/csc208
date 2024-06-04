## Brooks' Theorem
Any graph $G$ satisfies $\chi(G) \le \Delta(G)\text{,}$ unless $G$ is a complete graph or an odd cycle, in which case $\chi(G) = \Delta(G) + 1\text{.}$.

In other words any graph that is not a complete graph or odd cycle will have a maximum chromatic number that is equal or less than the largest degree of a vertice in a graph. 

This can be seen in the following graph:
![exampleofbrook](../resources/followsbrook.png)

The two exceptions to this theoreom are demonstrated by the following graphs:
![oddcycles](../resources/incorectoddcycle.png)
This is a graph with an odd cycle, which due to that aspect requieres for another color more than the highest degree for the vertices of the graph, 2.
![completegrap](../resources/completegraphbrook.png)
This is graph $K_4$ and due to completed graphs having all vertices connecting to every other vertices this means that all vertices need to have a different color as otherwise they wouldn't be properly colored. The highest degree for the vertices is 3 while we need 4 different colors to properly color the graph, demonstrating th exception in Brook's Theorem.

## 4. A group of 10 friends decides to head up to a cabin in the woods (where nothing could possibly go wrong). Unfortunately, a number of these friends have dated each other in the past, and things are still a little awkward. To get to the cabin, they need to divide up into some number of cars, and no two people who dated should be in the same car.

### A. What is the smallest number of cars you need if all the relationships were strictly heterosexual? Represent an example of such a situation with a graph. What kind of graph do you get?

If all relationships were strictly heterosexual then one representation of this would be the following:

![relationships](../resources/relationships.png)

If we look at this for a bit we will realize this is a bipartite graph. After all, bipartite graphs are graphs where we can divide the vertices into 2 sets of the vertices where they only connect to vertices from the other set, and we can color the graph's vertices using only 2 colors. These two sets are males and females as we are considering only heterosexual relationships between the 10 friends. Therefore the smallest number of cars is 2.

### B. Because a number of these friends dated there are also conflicts between friends of the same gender, listed below. Now what is the smallest number of conflict-free cars they could take to the cabin?




|  Friend  | A   | B   | C   | D   |  E   | F   | G   | H   | I   | J   |
|----------|-----|-----|-----|-----|------|-----|-----|-----|-----|-----|
| Conflicts:| CFG | J| AEF | H | CFG| ACEGI | EFI|D|AFG|B|


![noncolored](../resources/noncolored.png)

This graph is planar as none of the edges cross eachother. Therefore using The Four Color Theorem we know that the maximum amount of colors needed would be 4. Moreover, we see there is a cllique of 3 (a complete graph $K_3$) so the minimum amount of colors needed is 3. To actually find out how much needed we can evaluate this graph with this new information, however we can also solve is using networkx greedy coloring algorithm.

![colored](../resources/coloredrelationships.png)

## 5.What is the smallest number of colors that can be used to color the vertices of a cube so that no two adjacent vertices are colored identically?

To begin to solve this we first want to see if we can represent a cube as a planar graph. After all, this will then limit the maximum colors needed to four. Turns out we can!

![uncoloredcube](../resources/uncoloredcube.png)

Now we want to see if there are any cliques (complete graphs) to see if there is a minimum. There is actually only a clique of 2 present in this graph meaning the minimum is 2 colors.

![coloredcube](../resources/CUBE.png)

