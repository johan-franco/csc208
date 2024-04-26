# Chapter 3 (Symbolic Logic and Proofs) Notes:

## .1
- A proposition is a statement
- Propositional Logic studies how statements interact with eachother, the content of the proposition is not relevant to propositional logic
- When creating truth tables for a statement you want to break it up a lot depending on the statement
- Toulogy is when a statement is true solely based on the logical form, they don't give us a lot of info as no matter what it is true.
- Statements are logically equivalent if their truth table is the same.
- If you rephrase a statement in a logically equivalent method it can lead to insight on how to prove or refute.
- You can use boolean algebra to transform statements into others
- We can use morgan's laws and the fact that implications can be rewritten as disjunctions (and double negatives) to rewrite statements into other without using logic tables
- A deduction rule is when we have two statements together (both are true) cause the statement in the bottom to be true.
- To deduce a deduction rule you need to make a logic table and look where the statements are true



![logicConnectives](../resources/logicConnectives.png)

![negation](../resources/negation.png)

![morgan](../resources/MorganLaw.png)

![implications](../resources/implications.png)

## .2

- Simplest proof is a direct proof. Involves systematic explanation of what everything means. Good for solving implications
- General format for direct proofs are "Assume P ... ... Therefore Q
- Ensure whatever you are manipulating to a element that would prove your theory. This may involve breaking down what you are manipulating to explore what it means for you statement to be true.
- Proof by Contrapositive is essentially proving a different statement but is logically equivalent. For example if P implies Q and if not Q implies not P are logically equivalent, meaning through proving $\neg Q \implies \neg P $ you also prove $P \implies Q$.
- Structure for contrapositive proof is assume $\neg Q$ ... Therefore $\neg P$. 
- Note you do need to state you will prove through contrapositive in proof.
- In general i notice the use of let, suppose (or assume), in other words, then (or so), therefore (usually in this order).
- When doing contrapositives you may have to use de morgan laws and other laws to prove your proof is true. This is especially true if your statement does not tell you much (at its base )
- Some statements are not written as implications so you may have to rewrite it into one.
- Some statements cannot be transformed into a implication. You can try to solve these problems through contradiction.
- Trying to prove it by contradiction is essentially trying to prove $\neg P \implies Q$ is a false statement. Proving this means that P would have to be true.
- A lot of the practice problems prove by contradiction by demonstrating one side is odd and the other is even.
- it is not okay to prove a statement with solely a example. The only exception is existencial statements.
- One example of an existencial statement is there is an integer n such that $n^2-n+41$ is not prime. So to prove this we could have one example. This is called proof by counter example.
- When a statment is universal it makes it so the negation is existencial therefore you can prove a statmenet is false by providing a counterexample.
- Proof by cases is proving P is true by proving if Q implies P and if not Q then P. This demonstrates that P is always true regardless if Q is true or not.
- Essentially you may have to do this for statements where you aren't given much info and therefore have to show no matter how Q is changed then P is true.
- Contrapositive is logically equivalent to the original statement and would be $\neg Q \implies \neg P$
- Converse is not logically equivalent to original statement and would be $ Q \implies P$