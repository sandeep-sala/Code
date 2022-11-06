def reverse_alternate(s):
    return " ".join(
        [j.strip()[::-1] if (i + 1) % 2 == 0 else j.strip() for i, j in enumerate(s.split(" "))]
    )


print(reverse_alternate("Did it work?"), "Did ti work?")
print(
    reverse_alternate("I really hope it works this time..."),
    "I yllaer hope ti works siht time...",2
)
print(reverse_alternate("Reverse this string, please!"), "Reverse siht string, !esaelp")
print(reverse_alternate("Have a beer"), "Have a beer")
print(reverse_alternate(""), "")
