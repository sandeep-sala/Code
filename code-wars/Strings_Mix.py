def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        mx = max(val1, val2)
        if mx > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-mx, which + ":" + ch * mx)
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
print(mix(s1, s2))
