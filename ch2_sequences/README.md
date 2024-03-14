# Chapter 2 (Sequences) Notes:

## .1
- A sequence is  a ordered list of numbers, it cares extremely for order the numbers come in. However it can also be considered a type of function especially since we can manipulate sequences in similar manner to functions.
- For example $(a_n)_{n≥0}$ can be considered a function with a domain of all natural numbers and $a_n$ is the image (y).  
-  $(a_n)_{n∈N}$ or $(a_n)_{n≥0}$ refers to the full sequence.
- numbers in the subscripts are called indices. 
- Closed Formula is a formula that uses a fixed finite amount of operations on n (to calculate $a_n$ (image)). In other words if you are given n you should be able to solve for the image by simply plugging n in the formula.
- Recursive definition is an equation that relates a term to a previous term of a sequence and a intitial condition. Ex $a_n = 2a_{n−1}$ with $a_0 = 1$. Using this you would be unable to calculate the image directly with n as you need to first calculate $a_{n−1}$
- To find a closed formula you might have to find the recursive definition first
- We can look for patterns in a smaller sequence to attempt to apply to larger sequences.
- We can plug in what we believe is the closed formula into the recursive defintion to check if we are correct and check with the initial conditions as well.
- We can use sequences we know to compare to mystery sequences (essentially using other sequences we can define ones we don't know).
- Some sequences are the sum of terms in another sequence, usually we can express this in summation notation.
- Given any sequence $(a_n)n_{∈N}$, we can always form a new sequence
$(b_n)_{n∈N}$ by $b_n =  a_0 + a_1 + a_2 +$ $· · ·$  $+ a_n$
- This means that b_n can be called the sequence of partial sums of a_n (you can sometimes find the closed formula for b_n through a_n).