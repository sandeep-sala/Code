"""
Greedy Approach
1.Greedy - choice property : A global optimum can be arrived at by selecting a local optimum
2.Optimal Substructure : An optimal solution to the problem contains an optimal solutions to the subproblems


Problem: You have to make a change of an amount using the smallest possible number of coins.
Amount: $28

Available coins:
  $5 coin
  $2 coin
  $1 coin
"""
n = 38
coins = [5, 2, 1]
t_sum = 0
t = []
while t_sum <= n:
    for c in coins:
        if (c + t_sum) <= n:
            t_sum += c
            t.append(c)
            break
    if t_sum == n: break

        
print(t_sum)
print(t)