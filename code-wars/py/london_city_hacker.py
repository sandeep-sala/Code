def london_city_hacker(journey):
    c = 0.0
    prev = None
    for i in journey:
        if type(i) == str:
            c += 2.40
            prev = None
        else:
            if type(prev) == int:
                prev = None
            else:
                c += 1.50
                prev = i
    return "£{:.2f}".format(c)


print(london_city_hacker([12, 'Central', 'Circle', 21]), "£7.80")
print(london_city_hacker(['Piccadilly', 56]), "£3.90")
print(london_city_hacker(['Northern', 'Central', 'Circle']), "£7.20")
print(london_city_hacker(['Piccadilly', 56, 93, 243]), "£5.40")
print(london_city_hacker([386, 56, 1, 876]), "£3.00")
print(london_city_hacker([]), "£0.00")