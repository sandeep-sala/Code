def count_smileys(arr):
    c = 0
    for i in arr:
        d = 0
        if ":" in i or ";" in i:
            if ":" in i:
                i = i.replace(":", "")
            else:
                i = i.replace(";", "")
            d += 1
        if ")" in i or "D" in i:
            if ")" in i:
                i = i.replace(")", "")
            else:
                i = i.replace("D", "")
            d += 1
        if len(i) != 0:
            if not ("-" in i or "~" in i):
                d -= 1
        if d == 2:
            c += 1
    return c


print(count_smileys([]), 0)
print(count_smileys([':D', ':~)', ';~D', ':)']), 4)
print(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
print(count_smileys([';(', ':D', ':(', ':oD', ';oD', ';(', ';oD',
      ';o(', ';oD', ':D', ':D', ';-(', ';oD', ';-D', ';oD']), 4)
