def content_weight(b_w, scale): 
    return b_w - (b_w//(int(scale.split(" ")[0])+1)) if "larger" in scale else b_w//(int(scale.split(" ")[0])+1)
    
"""
def content_weight(w,s): 
    d,_,f=s.split();d=int(d)+1
    return w*(1 if f[0]=='s'else d-1)/d
"""

print(content_weight(120, "2 times larger"), 80)
print(content_weight(180, "2 times larger"), 120)
print(content_weight(500, "9 times larger"), 450)
print(content_weight(1000, "49 times larger"), 980)
print(content_weight(1000, "999 times larger"), 999)

print(content_weight(120, "2 times smaller"), 40)
print(content_weight(300, "2 times smaller"), 100)
print(content_weight(1000, "4 times smaller"), 200)
print(content_weight(1000, "49 times smaller"), 20)
print(content_weight(10000, "999 times smaller"), 10)