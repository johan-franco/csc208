## 1
The recursive formula is $a_n = a_{n-1} +2a_{n-2} $thus the next terms are 171 and 341.  This means that $a_n - a_{n-1} -2a_{n-2} = 0$ and can be represented as $x^2 -x-2$ solving for x results in (x-2)(x+1) thus the roots are x=2 and x=-1. Therefore we know now that the form will be $a_n = a2^n b-1^n$ which pluggin in 0 and 1 for n results in the following equations $3 = a +b$ and $5 = 2a-b$. Solving this system results in $ 5 = 2a -(3-a)$ simplyfing returns $ 8 = 3a$, $a = 8/3$ thus$ b = 1/3$. Finally the closed formula is a_n = 8/3(2^n)+1/3(-1^n)

## 3 
This can be rewritten as $ a_n - a{n-1} = 2^n$. Therefore we can use telescoping to rewrite this as $-a_0 + a_n = 2^{n+1} -2$ and since we know that $a_0 = 5$ we can simply it into $a_n = 2^{n+1} +3$

## 4 
We can check by pluggin $a_n = 4^n$ this results in $4^n = 3(4^{n-1}) + 4(4^{n-2})$ this can be further simplified into $4^n = 3(4^{n-1}) + 4^{n-1}$ and as multiplication is repeated addtion can be simplified into $4^n = 4^n$
