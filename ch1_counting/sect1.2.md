# Excercises

## 1 
There are $2^6 = 64$ subsets as each element is either added or not to a subset (yes or no). By limiting the amount of elements in the subset results in the amount of subsequent subsets turning into $2^3 = 8$. The subsets that do contain any odd numbers is the total amount of subsets subtracted by the subsets with only even numbers, resulting in $2^6 - 2^3= 56$. 

## 2
There are 15 sets with a cardinality of 4, I found this through multiplying $6*5*4*3$ and then dividing by $4*3*2*1$. There are 3 different subsets with cardinality of four that contain 2,3 and 5 meaning there is only 3 subsets with a cardinality of 4 that could have a subset of {2,3,5}. There are 3 even and odd numbers meaning it is impossible to avoid either at least one even or odd number. As there can only be 4 elements and there are 3 distinct even numbers, the subsets with cardinality of 4 that contain one even number are 3.

## 3
There are $2^9 = 512$ subsets of a. Using the same logic used for number 2 I found there were $\frac{\left(9\cdot8\cdot7\cdot6\cdot5\right)}{5\cdot4\cdot3\cdot2\cdot1} = 126$ subsets with a cardinality of 5. There are only 4 even numbers in the set so we just need to calculate the powerset of these four elements, {2,4,6,8}, which is $2^4 = 16$. I believe there 256 subsets with an even amount of elements, this is because the amount of subsets with 8 elements is equivalent to the number of elements with 1 element, 9. Since this pattern continues I strongly believe that the amount of even and odd subsets are equivalent.  

## 4
The amount of substrings with a length of 9 that start with 101, should be $2^6 = 64$ as the first three digits in the substrings are determined meaning there are only $2^6$ more possiblities. The start leaves use with already a weight of 2 meaning of the 6 more digits 3 have to be 1. Using recurrence relation we can realize $B^6_3 = B^5_2 + B^5_3$, and breaking it down further results in this, $B^6_3 = (B^4_1+B^4_2) + (B^4_2+B^4_3)$. We can then simplify the equation a bit to $B^6_3 = (4+(B^3_1+B^3_2)) + ((B^3_1+B^3_2)+4)$, which can be simplified to $B^6_3 = (4+6) + (4+6)= 20$.

There are $2^7 = 128$ substrings that end with 11. Adding this wil the substrings that start with 101 is 192, however there are substrings that complete both conditions that are being counted twice. To solve this issue we can calculate the substrings with both conditions, which is $2^4 = 16$ and then subtract it from our result. Therefore the amount of substrings that start or end with a certain substring are 176.

We already know the amount of substrings that have a weight of 5 and start with 101 (20) and we know that there are 128 substrings that end with 11. Using the same metholodgy as previously results in the following $B^7_3 = (B^5_1+B^5_2) + (B^5_2+B^5_3)$. This simplifies into $(5+10) + (10+ 10)=35$. Adding this to our 20 is 55. However we still need to subtract the duplicates that fufill both conditions, this is easily done understanding that only one of the digits can be 1 and that there are only 4 digits left, if both conditions are fufilled, resulting in this $B^4_1 = 4$ meaning the answer is 51.

## 5