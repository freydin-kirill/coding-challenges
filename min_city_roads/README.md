# Min City Roads

Level: *Medium*

**Problem**

It's no secret that some programmers really enjoy traveling. Well-known programmer, Petia, also loves traveling, visiting museums, and exploring landmarks in different cities. For his journeys between cities, he prefers to use a car. He refuels the car only at stations located within cities, not at stations along the road. Therefore, he carefully plans his routes to avoid running out of fuel on the road. Additionally, Petia is a crucial member of the team, so he can't afford to travel for too long. He decided to write a program to help him choose his next journey. However, due to his many other tasks, he asked for your assistance.

The distance between two cities is calculated as the sum of the absolute differences in coordinates along each axis. Roads exist between all pairs of cities.

**Input:**
- The first line contains the number of cities, n (2 ≤ n ≤ 1000).
- The following n lines contain two integers each: the coordinates of each city. The coordinates do not exceed a billion in absolute value. All cities are numbered from 1 to n in the order given in the input.
- The next line contains a positive integer, k, not exceeding two billion, which represents the maximum distance Petia can travel without refueling the car.
- The last line contains two different numbers: the number of the city where Petia starts and the number of the city where he is headed.

**Output:**
- If paths satisfying the aforementioned conditions exist, output the minimum number of roads that need to be traveled to reach the destination city from the starting point.
- If such paths do not exist, output -1.

**Example 1:**
Input:
```
7
0 0
0 2
2 2
0 -2
2 -2
2 -1
2 1
2
1 3
```
Output:
```
2
```

**Example 2:**
Input:
```
4
0 0
2 0
0 2
2 2
1
1 4
```
Output:
```
-1
```