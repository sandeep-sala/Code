import re
try:
    for _ in range(int(input())):
        print(sum(map(int, re.findall("\d", input()))))
except:
    pass
