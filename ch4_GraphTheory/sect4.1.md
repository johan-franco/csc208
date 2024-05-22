# Exercises

## Example 4.1.7.
We can think of each mathmetician as a seperate vertice. The questions asks if it is possible for each mathmetician to have shaken their hands with exatly 7 people. This means that the degree sequence would be (7,7,7,7,7,7,7,7,7), which is a total of 63. The Handshake Lemma states that the sum of all degrees of vertices should be even therefore, this is impossible.

## 1.
If each person is shaking hands with eachother and there are 10 people, this represents a complete graph of 10 vertices. Moreover, as a handshake is an event that occurs with two people (and then counts as one) it represents a edge. With this in mind, we can apply Handshake Lemma to find the amount of handshakes and as it is a complete graph each person (vertex) has a degree of 9. This means adding them all is 90, which when divided by two is 45, therefore there have been 45 handshakes. 

In relation to graph theory, this question is related to significantly given what I said previously. Each person exchanging handshakes with all other people makes the problem a complete graph as each person is representative as a vertice and each handshake as a edge.

## 2.
Every person represents a vertice and as being friends with someone is something that involves 2 people (and not counted twice) it represents a edge. Therefore the degree of everyone should be 2 meaning the sum of them all is 10 and as it is even it is possible as the sum of every degree needs to be even.

With 3 people in the group this would mean that the sum of the degrees is 15. This is impossible as the edges should be half of the sum of degrees and you cannot have .5 of a edge.

## 3. 


## 4
Graph 2 has a degree sequence of {3,3,2,2,2}
Graph 1 has a degree sequence of {3,3,2,2,2}

Given that both seem to respect the edge relation, there is reasonable evidence that the two are isomorphic.


## 5
Graph 1 has a degree sequence of {5,3,3,3,2,2,2}
Graph 2 has a degree sequence of {5,3,3,3,2,2,2}

## 6
The largest number of edges would be represented through $K_{10}$. Meaning the highest possible degree of every vertice would be 9 (cant connect to yourself). Therefore the sum of this 90 divided by 2, 45 represents the amount of edges possible (using Handshake Lemma).

A biparite graph simply means that you would be able to disjoint the vertices into two sets where all of set a isn't connected to eachother (and set b isn't connected to eachother). Therefore this would limit the connections by potentially one, depending on how we split it. Though it would make sense to have it split evenly. After all if we split it evenly then they would be be able to make connections with 5 other vertices (because they can't connect to themselves and the others in their set) if we multiply that by 10 we get 50, which we divide by 2 as otherwise we would be counting the edges twice for each edge, so we would have 25 edges. If we were to split the vertices 1 to 9. This would mean that there are 9 edges in total as the 9 can't connect with the vertices in their group, only with the sole edge. 

Trees essentially just can't have edges where they would be connected to other edges that could lead you to where you started. If the edges and number of vertices were equal there would have to be a cycle, meaning that if there are 10 vertices the maximum edges should be 9 as otherwise there should be a cycle.

## 7


The image above demonstrates how all graphs except 3 are biparite. After all, no matter how we label 3 the result will be two As connecting with eachother or two Bs.

## 8 
$C_n$ means the graph has a cycle of n vertices, in other words it is a huge loop (technically through removing one edge we would create a tree). Now if we were to attempt to check if $C_3$ was biparite we would realize it isn't, as an odd amount of vertices results in two vertices in the same set to be connected. This is because in one big loop (cycle) we would have to continue alternating from a to b for each vertex (otherwise it wouldn't be biparite), which means that whether it is biparite or not depends on what set the vertex we start on and the set of the vertex we end with as the two vertices are connected (else it would not be a big loop). Anyway, because we are alternating we can think of all odd numbers as either set A or B and all even numbers as set A or B. We will always start with an odd number (1), therefore we have to end on a even number. Therefore $C_n$ is biparite if n = 2(k), for some integer k (and n is larger than 3).

## 10
The subgraph of a complete graph is not necessarily complete. This is because subgraphs only need to have part of the graph, meaning it won't necessarily have all the edges between each vertex. For example if I had a complete graph with 5 vertices and if I then had 5 vertices connected in some manner with edges (but not completed) that would be a subgraph, which would also not be connected. 

Induced subgraphs mean that the subgraph for the vertices it has also has the same edges that it is a subgraph of. This would mean it is true that the induced subgraph of a complete graph is also a complete graph. After all, the complete graph has all the edges between the vertices meaning the induced subgraph's vertices also must have all the possible connections between them, which means it would be a complete graph.

