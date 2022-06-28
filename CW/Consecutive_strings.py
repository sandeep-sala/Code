def longest_consec(strarr, k):
    d = {}
    n = len(strarr)

    if n == 0 or k > n or k <= 0:
        return ""

    for i in range(n):
        tr = "".join(strarr[i:i+k])
        cr = len(tr)
        if cr not in d:
            d[cr] = tr

    if d:
        return d[max(d)]
    else:
        return ""


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
print(longest_consec([], 3), "")
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")