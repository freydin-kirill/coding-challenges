# Maximize It!

Source: *HackerRank*

Level: *Hard*

You are given a function $f(x) = x^2$ . You are also given `K` lists. The $i^(th)$ list consists of $N_i$ elements.

You have to pick one element from each list so that the value from the equation below is maximized:

$S = (f(X_1) + f(X_2) + ... +f(X_k)) \% M$

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

**Input Format**

The first line contains 2 space separated integers `K` and `M`.
The next `K` lines each contains an integer $N_i$, denoting the number of elements in the $i^(th)$ list, followed by $N_i$ space separated integers denoting the elements in the list.

**Output Format**

Output a single integer denoting the value $S_(max)$.

**Sample Input**
```
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
```
**Sample Output**

```
206
```

**Explanation**

Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum `S` value equal to $(5^2 + 9^2 + 10^2) \% 1000 = 206$.