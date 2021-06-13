def odd_or_even(arr):
    return "even" if sum(arr)%2==0 else "odd"


odd_or_even = lambda r: "even" if sum(r)%2==0 else "odd"

print(odd_or_even([0, 1, 2]), "odd")
print(odd_or_even([0, 1, 3]), "even")
print(odd_or_even([1023, 1, 2]), "even")