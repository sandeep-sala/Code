# def solution(s):
#     ans = []
#     for i in range(0, len(s), 2):
#         p = s[i:i+2]
#         if len(p) == 2:
#             ans.append(p)
#         else:
#             ans.append(p[0]+"_")
#     return ans

import re

def solution(s):
    return re.findall(".{2}", s + "_")


"dsad".split()

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    print(solution(inp), exp)