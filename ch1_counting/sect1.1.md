# Excercises

## 1

The answer is 5 * 3 * 17, which is 255. This was calculated using the multiplicative principle, which can be used as when you choose a shirt you still have to choose 1 of your three pants and 17 bowties.

## 2

A) Assuming you have to only wear one then you have 8 different options for neck-wear (as you cannot choose another).

B) If you must wear one of both then you have 3*5 options, which is 15.

C) We have the orginal 15 options (3 * 5), and the shirts are chosen with either a skirt or pants meaning the choices is added by 5(shirts) * 7(skirts and pants added). Additionally, you can simply wear a dress which would not need a shirt or pant. Therefore the equation should be the following 5 * 7 + 7 = 42 outfits.

## 3

a) This would be the answer if the question were to be if I can only watch one movie how many options do I have?

b) 63 would be the answer if the question was if I watch one comedy and one horror movie how many choices do I have?

## 4

a) The total combinations of these two sets are 16 * 16, which is 256. The chance for it to be E or F for the first digit is 2/16 meaning there is a 32/256 that a digit is E or F.

b) The reason why the principle you use does not matter is because the crux of the question only involves set A. There is no reliance on set B, if there was then you would have to use the multiplicative principle.

c) It should be 6/16 * 10/16 = 15/64, 15/64*4096(total combinations for 3 digits)=960 as there are 6 letters and 10 digits inbetween, which would then be multiplied together as it says 'and'.

d) There should be 1536 3 digit hexadecimal (6/16*4096) that start with A-F, 2560 that end with 0-9 and ones that start and end with both would be 960.

## 5

a) The largest possible intersection would be 10 as A is the smallest of the two sets with a size of 10.

b) The smallest amount of elements that they could have in common is 0.

c) The possible values are inbetween 15 and 25 because at most they can have 10 values in common ( set B has 15 values) or have none in common meaning set A and B would be added, equaling 25.

## 6

Even though we don't know if they have any intersection in elements the anwer is 13 as we calculate |A ∪ B| though this formula: |A ∪ B| − |A ∩ B|, which cancels out the unknown element into 13.

## 7
The answer is 39. We know that if everyone watched one show then it would be 28+19+24=71, however since we know that isn't the case and some watched 2 of the shows we can subtract that from the total count, 28+19+24-10-16-14=31. This would be the end if 8 hadn't watched all the shows meaning that the number we subtracted was too great, which is why we add the eight people back in resulting in 39 people.

## 8

15 + 20 + 9 = 44 (amount if everyone said they like only one type of potato)
44 - 12 - 5 - 6 + 3 = 24 (people that liked all types)= 21 (subtracts all that liked two types of potatoes or more)
24 is the number of individuals that at least like one type of potato, meaning 6 people in total hate potatoes in the school.

## 9
We can calculate the number of mutiples of 5, 6 and 7 by having them be divided by 100 and truncating the decimal, 100 + 83 + 71 = 254. However, this includes some mutiples repeatedly, which we can fix by dividing 83 by 7, 71 by 5, 83 by 5 truncating the decimal and subtracting from 254. The reasoning behind this is that 6 has 83 mutiples in 500 and each 7th one will be a multiple that 7 shares with 6, which is why we subtract from the total and do the same with 5. 

## 10 
Same principle as before we divide 1000 by our numbers, 3, 5 and 7 (333+142+200 = 675). Now because we are including mutiples that 3, 5 and 7 share we have to subtract or exclude these values. The number of these values can be determined by dividing and truncating the amount of times each fit into 1000. However unlike the other 3, 5, 7 have values that they all share like 105 meaning we have to add a value, otherwise we would exclude to much. This resulted in 542 (rounding up) as my answer, $$333+142+200-\left(\frac{333}{7}\right)-\left(\frac{142}{5}\right)-\frac{333}{5}+\frac{\frac{333}{5}}{7} = 542$$