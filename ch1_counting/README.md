# Chapter 1 (counting) Notes:

## .1

- Additive Principle states that if two event (A, B) occur in unrelated/disjoint (disjoin meaning that these two events can't occur at the same time) ways then the events of A and B can occur in a + b ways.
- The multiplicative principle states that if event A can occur in m
ways, and each possibility for A allows for exactly n ways for event
B, then the event “A and B” can occur in m · n ways. In other words if the choices aren't disjoint use the multiplicative principle.
- The word 'and' does not mean multiplication, there are cases were an event can change the next preceding event (which wouldn't make it a simple multiplicative problem)
- The additive principle with sets that have no common elements is |A ∪ B| = |A| + |B| .
- The Cartesian Product is the following: A × B = {(x, y) : x ∈ A ∧ y ∈ B}. In it x is a element of A and y is a element of B. The result of finding the cartesian product should be a set of ordered pairs.
- Multiplicative Principle with sets is defined as the following: Given two sets A and B, we have |A × B|  |A| · |B|.
- This is the cardinality of two sets: |A ∪ B| = |A| + |B| − |A ∩ B| (It does not matter if both sets share values as we subtract the duplicated values in the calculation)
- Cardinality for three sets: |A ∪ B ∪ C| = |A|+|B|+|C|−|A ∩ B|−|A ∩ C|−|B ∩ C|+|A ∩ B ∩ C|.

## .2

- Multiplicative principle is used to find the amount of subsets of a set (|P(A)|).
- To find the total amount of subsets with a certain amount of elements we can use the multiplicative principle and then divide by the amount of outcomes that are the same. This is due to the principle including sets like {3, 5, 2} and {5, 3, 2}.
- Bit string is a string of binary digits.
- The number of 1's in a string is the weight of the bit string.
- The length of a bit string does not discrimanate from 1 or 0.
- $B^n$ is the set of all n-bit strings.
- $B^n_k$ is the set of all n-bit strings of weight k.
- Recurrence relation is when we use one instance of our counting problem in terms of two simpler instances of the problem.
- Integer Lattice is the set of all points in the Cartesian plane for which
both the x and y coordinates are integers like the the intersections of the grid lines. 
- Latice path is one of the shortest possible paths connecting two points on the lattice, moving only horizontally and vertically. 
- We can determine length of paths through how many steps a latice path has.
- Bit strings can represent paths meaning that latice points and bit strings share the same reccurence relation.
- Binomial coefficients are specificallty the coefficients of a binomial that is fully expanded.
- $^n_k$ is a symbol for binomial coeeficients
- Binomial Coefficients are also related to recurrence relation
- $|B^n_k| = |B^{n-1}_{K-1}| + |B^{n-1}_k|$
