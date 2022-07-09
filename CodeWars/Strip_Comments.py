def solution(string,markers):
    l = string.split("\n")
    k = []
    for i in l:
        if len(set(i).intersection(set(markers)))==0:
            k.append(i.strip())
        else:
            kk = [ i.index(k) for k in markers if k in i]
            k.append( i[:min(kk)].strip() )
    return "\n".join(k)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("a #b\nc\nd $e f g", ["#", "$"]))