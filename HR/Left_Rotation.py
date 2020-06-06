import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    for i in range(d):
        a.append(a[0])
        del a[0]
    print(" ".join(list(map(str ,a ))))