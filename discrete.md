# Discrete Math

Discrete Mathematics is a branch of mathematics that deals with objects that can assume only distinct, separated values. Unlike continuous mathematics, where the concepts of calculus and real analysis are focused on topics that vary smoothly, discrete mathematics covers areas such as combinatorics, graph theory, and the theory of computation. It includes the study of algorithms, integers, graphs, and statements in logic. Discrete mathematics is fundamental to computer science, as it is concerned with the study of algorithms, data structures, and the efficiency of algorithms. It also plays a critical role in cryptography, logic, discrete probability, and the design of computer networks.


## Why is it called discrete
Discrete mathematics is called "discrete" because it deals with distinct, separate values or objects. The term "discrete" contrasts with "continuous." In discrete mathematics, we study entities that can be counted as separate and distinct units. This distinction is crucial for understanding the nature of problems and phenomena that discrete mathematics aims to address.

Distinct Elements: The subjects of study in discrete mathematics, such as integers, graphs, and logical statements, are characterized by their separateness. For example, when dealing with integers, we consider individual numbers like 1, 2, 3, etc., without considering the values in between, unlike in continuous mathematics where you might consider every possible value within an interval, such as all real numbers between 0 and 1.

Countable Nature: Many areas of discrete mathematics involve structures that are countable or finite in nature. For instance, when examining a finite graph, the number of vertices (nodes) and edges (connections between nodes) can be counted, and each vertex and edge is treated as a discrete entity.

Discrete Structures: Discrete mathematics often involves the study of discrete structures, such as sets, graphs, and sequences, which are composed of distinct and well-defined elements. These structures do not blend seamlessly into each other but instead maintain their individuality within the context of the structure.

Applicability to Digital Systems: The discrete nature of this branch of mathematics aligns well with the binary nature of computing and digital systems, where data is represented in binary (0s and 1s) and processed in discrete steps. This is a key reason why discrete mathematics is fundamental to computer science and information technology.


## Examples
### Graph Theory:
- Representing a network of roads and cities as a graph, where cities are nodes (vertices) and roads are edges connecting these nodes. This representation can help in solving problems like finding the shortest path between two cities.
Combinatorics:

### Combinatorics:
- Counting the number of possible combinations of passwords made from a 6-character alphanumeric set (letters and numbers). Combinatorics helps in understanding the principles of counting and arranging objects.
Logic:

### Logic:
Example: Evaluating the truth of logical statements and using logical operators. For instance, determining the truth value of a statement like "If it is raining, then the ground is wet" and its contrapositive, inverse, and converse statements.


### Set Theory:
- Analyzing relationships between sets through operations like union, intersection, and complement. For example, considering the set of all students in a school and the set of all students enrolled in a math class to find those enrolled in both or just one.
Algorithms:

### Algorithms:
- Designing a step-by-step procedure for sorting a list of numbers from smallest to largest using algorithms like bubble sort or quicksort. Algorithms are central to computing and data processing tasks.
Discrete Probability:

### Discrete Probability:
- Calculating the probability of rolling a sum of 7 with two dice. Discrete probability deals with events that have a countable number of outcomes.

### Number Theory:
- Exploring properties of integers, such as divisibility, the greatest common divisor, and prime numbers. An application of number theory is in cryptography, such as the RSA algorithm which relies on the difficulty of factoring large prime numbers.
Cryptography:

### Cryptography:
- Example: Using mathematical principles to design secure communication protocols. This includes creating and breaking encryption and decryption algorithms to protect information from unauthorized access.
Finite State Machines:

### Finite State Machines:
- Modeling a vending machine that dispenses products when a certain amount of money has been inserted, transitioning through states based on input (money inserted, product selected, etc.).

### Practice Exercises

1. If a set B has n elements, then what is the total number of subsets of B. Justify your answer.

2. Three friends play marbles each week. When they combine their marbles, they have 100 in total. 45 of the marbles are new and the rest are old. 30 are red, 20 are green, 25 are yellow, and the rest are white. What is the probability that a randomly chosen marble is new OR yellow? (discrete probability)

3. Find out the number of ways that the letters of the word “LEADER” can be arranged?

Problem 1 Solution:
If a set B has “n” elements, then the total number of subsets of B is 2<sup>n</sup>. For example, if B contains 5 elements, say B = {1, 2, 3, 4, 5}, then the total number of subsets of B is 2<sup>5</sup> = 32.


Problem 2 Solution:
We get the following probabilities for the New Marbles and Yellow Marbles: $$\Large\frac{45}{100}, \frac{25}{100}$$
To calculate the possibility of the marbles being new or yellow we must account for the marbles that are both new and yellow, which is: $$\Large\frac{45}{100} * \frac{25}{100}$$
Meaning the probability for a marble to be new or yellow can be represented by the following:
$$\Large\frac{45}{100} + \frac{25}{100} - \frac{45}{100} * \frac{25}{100}$$
Solving results in:  $$\Large\frac{47}{80} $$

Problem 3 Solution:
In the word “LEADER”, there are 6 letters. In that, E is repeated twice. Hence, the total number of ways that the letters can be arranged = 6!/2! As we know, 6! = 720 and 2! = 2 Therefore, the number of ways that the letters can be arranged = 720/2 = 360.



[Discrete Math Problems](https://byjus.com/maths/discrete-mathematics-questions/)
[Discrete mathematics](https://brilliant.org/wiki/discrete-mathematics/#:~:text=Discrete%20mathematics%20is%20the%20study,can%20be%20finite%20or%20infinite.)
[Discrete mathematics](https://en.wikipedia.org/wiki/Discrete_mathematics)
[Learn more](https://www.geeksforgeeks.org/discrete-mathematics-tutorial/)
[Problem 2 Link](https://www.varsitytutors.com/gmat_math-help/arithmetic/problem-solving-questions/discrete-probability)
