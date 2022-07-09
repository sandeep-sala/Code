# Problem are broken down to smaller problem recursvely 
# solution to subproblem combined to originla problem

# Merge sort
# Quick sort
# Fibonacci Series


# Number Factor
# House Robber
# Convert String
# Zero One Knapsack Problem
# Longest Common Subsequence (LCS)

def numberFactor(n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subp1 = numberFactor(n-1)
        subp2 = numberFactor(n-3)
        subp3 = numberFactor(n-4)
        return subp1+subp2+subp3

# print(numberFactor(5))


def houseRobber(houses, currentHouse = 0):
    if currentHouse >= len(houses):
        return 0
    stealFirstHouse = houses[currentHouse] + houseRobber(houses, currentHouse+2)
    skipFistHouse = houseRobber(houses, currentHouse+1)
    return max(stealFirstHouse,skipFistHouse)

# houses = [6,7,1,30,8,2,4]
# print(houseRobber(houses))

def findMinOperation(s1, s2, index1=0, index2=0):
    if index1 ==  len(s1):
        return len(s2) - index2
    if index2 ==  len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1)
    else:
        delOp = 1 + findMinOperation(s1, s2, index1, index2+1)
        insOp = 1 + findMinOperation(s1, s2, index1+1, index2)
        repOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
        return min(delOp,insOp,repOp)

# print(findMinOperation("table", "tbrles"))


class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zoKnapsack(items, capacity, currentIndex=0):
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = zoKnapsack(items, capacity, currentIndex+1)
        return max(profit1,profit2)
    else:
        return 0

# print(zoKnapsack([
#     Item(31,3),
#     Item(26,1),
#     Item(17,2),
#     Item(72,5),
# ],7))