# Exercises

## 1

### A
$(P\lor Q) \implies Q $
It is your birthday is represented by P and there is cake is represented by Q.

### B
+-----+-----+------------+----------------------+
|  p  |  q  |  (p or q)  |  (p or q) implies q  |
|-----+-----+------------+----------------------|
|  1  |  1  |     1      |          1           |
|  1  |  0  |     1      |          0           |
|  0  |  1  |     1      |          1           |
|  0  |  0  |     0      |          1           |
+-----+-----+------------+----------------------+
### C
If Q is true (and the whole statement) then all we can conclude is that the whole statement will be true and that there will be cake, it doesn't mean it is our birthday though.
### D
If the statement is true and there will not be cake then we can assume it is not our birthday.

### E
If the statement is wrong then there will be no cake despite it being our birthday.

## 2
``` txt
+-----+-----+------------+-------------+------------------------------+
|  p  |  q  |  (p or q)  |  (p and q)  |  (p or q) implies (p and q)  |
|-----+-----+------------+-------------+------------------------------|
|  1  |  1  |     1      |      1      |              1               |
|  1  |  0  |     1      |      0      |              0               |
|  0  |  1  |     1      |      0      |              0               |
|  0  |  0  |     0      |      0      |              1               |
+-----+-----+------------+-------------+------------------------------+
```
## 3
``` txt
+-----+-----+-----------+-----------------+-----------------------------+
|  p  |  q  |  (not p)  |  (q implies p)  |  (not p) and (q implies p)  |
|-----+-----+-----------+-----------------+-----------------------------|
|  1  |  1  |     0     |        1        |              0              |
|  1  |  0  |     0     |        1        |              0              |
|  0  |  1  |     1     |        0        |              0              |
|  0  |  0  |     1     |        1        |              1              |
+-----+-----+-----------+-----------------+-----------------------------+
```
## 4

``` txt
+-----+-----+-----+------+-----------+------------------------+   
|  p  |  q  |  r  |  ~p  |  q and r  |  ~p implies (q and r)  |   
|-----+-----+-----+------+-----------+------------------------|   
|  1  |  1  |  1  |  0   |     1     |           1            | 
|  1  |  1  |  0  |  0   |     0     |           1            |  
|  1  |  0  |  1  |  0   |     0     |           1            |   
|  1  |  0  |  0  |  0   |     0     |           1            |   
|  0  |  1  |  1  |  1   |     1     |           1            |   
|  0  |  1  |  0  |  1   |     0     |           0            |   
|  0  |  0  |  1  |  1   |     0     |           0            | 
|  0  |  0  |  0  |  1   |     0     |           0            |
+-----+-----+-----+------+-----------+------------------------+
```

## 5

Either or implies that Geoff won't have both sausage and pepperoni (S or Q)
