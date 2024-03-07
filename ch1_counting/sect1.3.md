# Exercises
## 1
We can use the formula for combinations as the order of toppings doesn't matter (in the sense that the same toppings rearranged in a different order is not a new topping order). This results in the following $\frac{10!}{(10-3)!3!} = 120$

We can use the multiplicative principle to solve the second part as there are 10 different toppings that we either say yes or no to. $2^10 = 1024$ pizzas

We can calculate the amount of methods to arrange the left column by realizing there are 10 different topping and 5 spots, where order does matter as the placement of a topping in the top or bottom of the column does matter. This means that we can use the permutation formula resulting in: $\frac{10!}{5!} = 30240 $ arrangements.

## 2
This problem is a permutation as the order of each number do matter and it is specified that each of the three numbers is distinct. This results in the following: $\frac{40!}{37!} = 59280$ different combinations.

## 3
There are 7 digits from 2 to 8. Moreover, we always have 7 choices as in this situation numbers can be repeated. This means we can use the multiplicative principle as there are 7 choices and we need to choose 5 numbers, therefore, $7^5 = 16807$ different 5 digit numbers.

This is a permutation as the problem asks for numbers to not be repeated but states that they can come in any order. $P(7,5) = \frac{7!}{(7-5)!} = 2520$ different 5 digit numbers. 

To come in increasing order  means that this problem is a combination as it wants the number to now be a certain way. This result in $^7_5 = \frac{7!}{(7-5)!5!} = 21$

The second problem is a permutation as it asks for distinct numbers in any order. The third problem is a combination as the problem asks for the numbers to be in a increasing order, which you can view as the problem asking for a problem in one certain order, which is what combinations calculate.

## 4
To find the methods we can use to rearrange the books we can use the permutation formula because the problem states that the books can be in any order. This results in $P(17,10) = \frac{17!}{7!} = 7.05729024×10^{10} $.

If they need to be in alphabetical order than we have a combination problem with the following result, $^17_10 = \frac{17!}{7!10!} = 19448$ combinations.

## 5 
The dots have a height of 2 while the dots horizontally are 7. Squares would be 2 units vertically and 2 units horizontally. (I had trouble trying to calculate)

## 6 
Using only a height of one and the orgin point we can make 6 triangles using the others horizontally. If we maintain the same height but move right by one we can make 5 triangles this pattern continues for a height of one, so with a height of one we can make $6+5+4+3+2+1 = 21$. We have a total height of 4 and this pattern also continues meaning we can multiply twenty one by four, which equals $84$. Now if we attempt to do the same thing with the height we realize that the pattern is $4 + 3 + 2 + 1 = 10$. However, if we were to multiply this we would be counting the right triangles twice (they were accounted for already when we calculated the total amount of triangles you can make with 2 vertices on the horizonatal), meaning the pattern is actually $3+2+1 = 6$, which multiply by the length six is equal to $36$. Adding our two numbers results in the following, $36+84 = 120$.

## 7 
This results in the following $15! = 1.307674368×10^12$ anagrams of uncopyrightable. 

## 8
I believe we simply act like 'a' is the beginnning of the anagram and then take the combination of rest of the elements. This results in $^7_5 = \frac{7!}{5!\times2!} = 21$. This is because there are 21 different ways to place the 5 's' in assesses meaning there is only 21 unique anagrams that start with 
'a'.

## 9
We have 'a' repeating 3 times meaning we must ensure that all 3 are being placed in differing unique places which we can do by recognizing that the length of 'anagram' is 7. This results in $^7_3 = \frac{7!}{4!\times3!} = 35$. There are no more repeating elemnts meaning we can multiply the $35$ by $4!$ as it represents the unique places that the rest of the distinct elements can go, this results in $840$.

## 10
Using combinations we can find the answer. $^20_4$ (in total 20 people and 4 groups of people) represents the total amount of unique groups can be made for the first group. Since we made the first group already we have less people meaning the unique groups that can be made for the second group is represented by $^16_4$. This continues for all five groups, it can be represented by the following, $(^{20}_4)(^{16}_4)(^{12}_4)(^8_4)(^4_4)  = 3.05540235×10^11$

If each group has to have a board member all we have to do is subtract the total amount of people by 5 (k) and the number of people in each group by 1 (n). This results in the following $(^{15}_3)(^{12}_3)(^{9}_3)(^6_3)(^3_3)  = 168168000$ combinations of 3 man groups. Now we have to calculate the number of ways the board members can be arranged which is represented by $5!$, meaning the total number of cominations is $2.018016×10^10$. 

## 11
If King Arthur is also considered in the rearrangement then there are $10!$. I assume that King Arthur would stay on his throne though so there is $9! = 362880$ ways to rearrange seating. 

## 12