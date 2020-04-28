import os
import sys

def twoStacks(x, a, b):
    c = 0
    return c


if __name__ == '__main__':
    g = int(input())
    for g_itr in range(g):
        nmx = input().split()
        n = int(nmx[0])
        m = int(nmx[1])
        x = int(nmx[2])
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        result = twoStacks(x, a, b)
        print(result)
