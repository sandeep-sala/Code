def count_sheep(n):
    return "".join([ f"{i} sheep..." for i in range(1,n+1)])

print(count_sheep(0), "");
print(count_sheep(1), "1 sheep...");
print(count_sheep(2), "1 sheep...2 sheep...")
print(count_sheep(3), "1 sheep...2 sheep...3 sheep...")