# Exercises

## 15. Prove that every connected graph which is not itself a tree must have at last three different (although possibly isomorphic) spanning trees.

Understand the following:
- A connected graph means that every vertex has an edge that connects it to the rest of the graph
- A tree is a connected graph in itself that simply contains no cycles (so no loops).
- A spanning tree is a subgraph that is a tree with all the vertices of the graph it was a connected subgraph of.
- The minimum of vertices needed to create a cycle is 3 as a cycle is a loop/path that starts and stops on the same vertex without containing repeated vertices.
- Therefore if we prove that you can make 3 spanning trees from the minimum amount of vertices needed to create a cycle, this should be true.
- 


## 7 
### (A) We define a forest to be a graph with no cycles. Explain why this is a good name. That is, explain why a forest is a union of trees.
Other than having no cycles forests also don't need to have all vertices connected, while trees do.  If we were to have a forest with 3 disconnected groups of vertices, (all the vertices in a group are connected to eachother only) we could say that the forest is a union of three trees. After all, each if we were to take a subgraphs of the 3 groups it would result into 3 different trees.

### (B) Suppose F is a forest consisting of m trees and v vertices. How many edges does F have? Explain
A single tree has $n - 1$ edges. This is because in order for a tree to be connected there needs to enough edges for all vertices to be connected but also not too much for a cycle to occur. Anyway with this in mind as for each tree in the forest we would have one less edge there are $v-m$ edges in F.

