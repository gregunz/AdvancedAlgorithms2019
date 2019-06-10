# Advanced Algorithms Course (CS-450 @EPFL) Spring 2019 - Homework

Theoretical course - Few implementations of the algorithms seen in class:

# [1.](1_HikingTrails.py) Three-way Hiking Trails

It's the second year of your job as the Swiss Hiking Minister. During the past year, you managed to complete the first phase of an ambitious new project - a network of Three-way Hiking Trails! Each 3-way hiking trail connects three different mountain huts, and you have m such trails and n mountain huts numbered 1 to n.

In the second phase of the project, you need to ensure that every trail is reachable. That is, at least one of the three mountain huts that it connects must be upgraded to become a train station. It costs c_i CHF to upgrade the i-th hut to a station. You would like to select a set of huts to upgrade whose total cost is as low as possible.

As this sounds like a difficult challenge, you do not need to compute the best possible solution. However, taxpayer money cannot be wasted: your solution must be at most three times more expensive than the cheapest one.

For reasons of transparency, you will need to provide evidence that this is the case. You will do so by assigning a nonnegative integer budget to each trail. These budgets must satisfy two conditions. First, the cost of your solution must stay within three times the budget, i.e., the sum of hut upgrade costs must be at most three times the sum of budgets of all trails. Second, for each hut (regardless of whether it will be upgraded), the sum of budgets of trails connected to it must be at most the upgrade cost for that hut.

If you cannot do it, the federal council will not approve your budget, and the whole project will be in jeopardy. Are you ready to save your precious project?

### Input

The first line of the input contains two space-separated integers n and m – the number of huts and the number of trails, respectively (2 ≤ n ≤ 200, 1 ≤ m ≤ 4000).

The second line contains n space-separated integers c_1, c_2, ..., c_n, where c_i is the cost of upgrading the i-th hut to a train station (1 ≤ c_i ≤ 10^6).

The following m lines describe the trails. The i-th of these lines describes the i-th trail and contains three space-separated integers u, vand w. (1 ≤ u < v < w ≤ n) that describe a three-way trail connecting the mountain huts numbered u, v, and w. The trails do not repeat.

### Output

Your program must print three lines.

On the first line, output the number k of huts in your solution (i.e., those that you will upgrade to train stations).

On the second line, output k space-separated integers v_1, v_2, ..., v_k – the numbers of these huts (1 ≤ v_i ≤ n). They can be printed in any order, but should not repeat.

On the third line, print m space-separated integers b_1, b_2, ..., b_m – the budgets that you have assigned to the trails, in the order in which the trails appear in the input (0 ≤ b_j ≤ 10^9).

If there are many possible correct solutions, you may output any of them.



## [2.](2_KargersAlgo.py) Karger's Algorithm

You are given a connected undirected graph (with possibly multiple edges between the same pair of vertices). Using Karger's min-cut algorithm, find and return the size of the minimum cut in the graph, as well as the number of minimum cuts.

### Input

The first line of the input contains two space-separated integers n and m (2 ≤ n ≤ 100, 1 ≤ m ≤ 400) – the number of vertices and the number of edges, respectively. The next m lines describe the edges. Each such line contains two space-separated integers a and b (1 ≤ a, b ≤ n, a ≠ b) – endpoints of the edge. There may be multiple edges between the same pair of vertices. The graph is connected.

### Output

Output two integers – the size of the minimum cut and the number of cuts of this size in the graph. Two cuts are different if the corresponding sets of edges are different.
