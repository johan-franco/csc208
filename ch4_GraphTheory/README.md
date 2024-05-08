# Chapter 4 Notes:

## .1
- Graph definition is a ordered pair $ G = (V,E)$. V is a set of the vertices and set E (called edges) is two element subset of V. Ex: $(\{a,b,c,d\}, \{\{a,b\}, \{ac\}, \{b,c\}\})$
\begin\{equation*\}
- Each vertex represents a dot and we connect them with lines based on set E
- This means there are various ways to represent a set when using graphs.
- Graphs that are basically the same (but perhaps not equal) are called isomorphic
- This means that graphs that are the complete same only with differing elements are isomorphic not equal.
- An isomorphism is simply a function which renames the vertices. It must be a bijection so every vertex gets a new name. Vertices must continue to be connected to edges in the same way they were previosly.
- To check if there is isomorphism what you may need is to draw the graphs for both (in the same way) and then you can notice similarities where you can swap or the differences in edges.
- To make sure that the function is an isomorphism, we must make sure it respects the edge relation.
-  A collection of isomorphic graphs is often called an isomorphism class
- Graphs with a special name like $K_n$ or without labels are refering to all graphs isomorphic to any copy of that particular graph.
- Graphs can be a subgraph of a larger number. 
- $G' = (V', E')$ is a subgraph of $G = (V, E)$. To demonstrate this we can write $G' \subseteq G$, moreover this implies that $V' \subseteq V$ and $E' \subseteq E$
- An Induced Subgraph of $G = (V, E)$ is provided when $V' \subseteq V$  and every edge in E
 whose vertices are still in V' is also an edge in E'. 
- I believe the difference would be lets say that E has vertices a b c d and E' had a b c. Then E has 3 edges connected to a, E' if it wants to be induced subgraph would have to have all three edges that are connecting to a but it can still be considered a subgraph even if it only contains 2.
- With what I previously stated it is clear that every induced subgraph is also an ordinary subgraph, but not conversely.
- The vertices are extremely important to determining if something is a subgraph. For example, if there is vertices a b  and c connected to eachother with a straight line, if another graph had both a and c arranged in the same way and connected to eachother it would not be a subgraph to the other as technically the other never had an edge that connected both a and c.
- If the graph has the  property that no pair of vertices is connected more than once, and no vertex is connected to itself then it may be called a simple graph. However no pair of vertices can be connected by an edge more than once. Also, since each edge must be a set containing two vertices, we cannot have a single vertex connected to itself by an edge, so the book continues to refer to them as graphs.
- Graphs that have double edges or single edge loops are called multigraphs. After all a multiset allows use to repeat use of a single element.
- Graphs are connected if you can get from any vertex to another vertex by following a path of edges.
- Graphs that aren't connected can be thought as two seperate graphs  (intersecting lines from seperated graphs do not make it connected)
- Every vertice usually does not have edges between, however if we were to add them all then the graph can be considered complete.
- There can only be one complete graph for a given amount of vertices, which we call $K_n$.
- Every vertex in a complete graph $K_n$ would be adjacent to n-1 vertices 
- The number of edges from a given vertex the degree of that vertex, so all $K_n$ vertices would have n-1 degree. Using this logic this means the amount of edges in $K_n$ is $n(n-1)/2$
- In general the sum of all vertices degrees will always be twice the amount of edges meaning the sum is even. This called the Handshake Lemma.
- LEmma can be written as this(d(v) represents degree of vertex v)$\sum_{v\in V} d(v) = 2e\text{.}$
- The degree sequence is a list of every degree of every vertex in the graph, generally written in non-increasing order, if you have you would be able to find the amount of edges.
- In any graph, the number of vertices with odd degree must be even.
- A graph is biparite if vertices can be divided into two sets, A and B with none of them having any adjacent vertices within themselves. However they can be adjacent to the vertices in the other set (a with b and b with a). 
- If each vertex in A is adjacent to all vertices in B then it is a complete biparite graph and receives the name of K_{mn} .

