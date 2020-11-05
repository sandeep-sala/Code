def rgb(r, g, b):
    if r < 0 : r = 0
    if g < 0 : g = 0
    if b < 0 : b = 0
    if r > 255 : r = 255
    if g > 255 : g = 255
    if b > 255 : b = 255
    return ('%02x%02x%02x' % (r, g, b)).upper()


print(rgb(0,0,0),"000000", "testing zero values")
print(rgb(1,2,3),"010203", "testing near zero values")
print(rgb(255,255,255), "FFFFFF", "testing max values")
print(rgb(254,253,252), "FEFDFC", "testing near max values")
print(rgb(-20,275,125), "00FF7D", "testing out of range values")