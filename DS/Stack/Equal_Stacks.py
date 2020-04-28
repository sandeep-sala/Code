import os
import sys

def equalStacks(h1, h2, h3):
    s1, s2, s3 = set(),set(),set()
    s=0
    for i in range(len(h1)):
        s += h1[i]
        s1.add(s)
    s=0
    print(s1)
    for i in range(len(h2)):
        s += h2[i]
        if s in s1:
            s2.add(s)
    s=0
    print(s2)
    for i in range(len(h3)):
        s += h3[i]
        if s in s2:
            s3.add(s)
    print(s3)
    return max(s3) if s3 else 0


if __name__ == '__main__':
    n1N2N3 = input().split()
    n1 = int(n1N2N3[0])
    n2 = int(n1N2N3[1])
    n3 = int(n1N2N3[2])
    h1 = list(map(int, input().rstrip().split()))[::-1]
    h2 = list(map(int, input().rstrip().split()))[::-1]
    h3 = list(map(int, input().rstrip().split()))[::-1]
    result = equalStacks(h1, h2, h3)
    print(result)
