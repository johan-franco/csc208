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

## .2
- Arthmetic Sequences are sequences that have a common difference of d. Its recursive definition is $ a_n = a_{n-1} + d$ with $a_0 = a$. The closed formula is $a_n = a + dn$.
- If the difference is not constant but the ratio between succesive terms is constant (constant ratio) then it is geometric sequence.
- Geometric sequences have a recursive definition of $ a_n = ra_{n-1}$ with $a_0 = a$ and a closed formula of $a_n = a * r^n$
- These formulas all are created with the assumption $a_0 = a$, which significantly simplifies the formula. 
- $T_n$ is the sequence of partial sums of the sequence 1, 2, 3 ...
- To add up terms in a arthmetic sequence we can essentially regroup them to facilitate adding.
- Doing this results in $T_n = n{n-1}/2.
- Sequences can also be interpreted as sequence of partial sums of arthmitic or geometric sequences.
- We can reverse and add to work out the sum for any arthmetic sequence. Essentially we add the first and last term, multiply it by the number of terms inbetween the two and then divide by two. Using this we can find closed formula for sequences of partial sums.
- We can find the sum of a geometric sequence through multiplying, shift and subtract. Essentially we multiply the sequence by its common ratio so each term transforms into the next term, we then subtract the sequence, which leaves us with either -S or S (depending on how you subtracted) equals 2 terms (simplify and thats your answer).
## .3
- $\Delta^k$-constant is what we call sequences that have kth differences that are all constant. So a $\Delta^3$-constant means the sequence has three differences (differences of differences of differences of the sequence)
- If we continue to take the differences of a sequence and are left with the same sequence then the that means no finite number of sequences will be constant thus it is not $\Delta^k$-constant.
- $\Delta^0$-constant means the closed formula is solely the number, $\Delta^1$-constant means a arthmetic sequence, $\Delta^2$-constant are the sum of an arthmetic sequence (closed formula is a quadratic).
- An increase in the number of differences means an increase in polynomial.
## .4
- Plug the closed formula into the recurrence relation to check if your closed formula is correct (should return your closed formula).
- Telescoping refers to the phenomenon when many terms in a large sum cancel out—so the sum “telescopes. Ex: $ (2 - 1) + (3 - 2) + (4 - 3) + \cdots + (100 - 99) + (101 - 100) = -1 + 101 $ This is because shifting the problem results in 2-2 and 3-3 but leaves -1 and 101.
- Telescoping can simplify recursive problems into closed formulas this can be done with a recursive problem that can be simplified into $a_n -a_{n-1}  = f(n).
- We can use iterating to also find the closed formula. Essentially you iterate the process of finding the next term, starting with the known initial condition, up until you have $a_n$
- Essentially if a reccurence relation follows $+a_n + \alpha a_{n-1} + \beta a_{n-2} = 0$ the characteristic polynomial is $x^2 + \alpha x + \beta $ which we can use to solve for r that results in us solving the occurence relation (where a and b are determined in intial conditions).
- If there is only root then $ a_n = ar^n + bnr^n $ is solution to the characteristic polynomial is 
## .5
- Inductive proof structure is first using a base case and than assuming your statement is true prove why P(k+1) is true.
- You start with Let P(n) be the statement ... and end with Therefore by the principle of mathematical induction, the statement P(n) is true for all  $n> 1$ (depends on what you are trying to prove).
- You want to understant the idea of the argument (what is occuring), which you do by increasing n. 