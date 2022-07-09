# Build Solution piece by piece
# In each step it chooses the most obvious/immediate benfits
# Best for --- sol wiht local optimal sol. leads to global sol.

# Insertion sort
# Selection sort
# Topological sort
# prims algo
# kruskal algo

# Activity Selection Problem
# Coin Change Problem
# Fractional Knapsack Problem


# Activity Selection Problem
def get_max_activities(activites):
    max_activites = []
    i = 0
    activites.sort(key=lambda x: x[2])
    max_activites.append(activites[0][0])
    for key,value in enumerate(activites[1:]):
        if value[1] >  activites[i][2]:
            max_activites.append(value[0])
            i = key
    return max_activites

activites = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 8, 9],
]

print( get_max_activities(activites) ) 

# Coin Change Problem
def coinChange(totalNumber,coins):
    N = totalNumber
    coins.sort()
    index = len(coins) -1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1
        if N == 0:
            break

coins = [1,2,5,20,50,100]
coinChange(203,coins)


# Fractional Knapsack Problem
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight

def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if totalValue == capacity:
            return totalValue
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unUsedWeight = capacity - usedCapacity
            value = i.ratio * unUsedWeight
            usedCapacity += unUsedWeight
            totalValue += value
    return totalValue

cList = [ Item(20,100),Item(30,120),Item(10,60) ]
print(knapsackMethod(cList, 50))