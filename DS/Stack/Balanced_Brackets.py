import os
import sys


# {[()]}
def isBalanced(s):
    k = []
    for i in s:
        if i == "(" or i == "[" or i == "{":
            k.append(i)
        else:
            if len(k) > 0:
                if (i == ")" and k[-1] == "(") or (i == "]" and k[-1] == "[") or (i == "}" and k[-1] == "{"):
                    k.pop()
                else:
                    return "NO"
            else:
                return "NO"
    if len(k) == 0:
        return "YES"
    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)
        # fptr.write(result + '\n')
    # fptr.close()
