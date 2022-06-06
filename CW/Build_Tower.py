def tower_builder(n): return [
    f"{ ('*'*((i*2)-1) ).center((n*2)-1) }" for i in range(1, n+1)]


print(tower_builder(1), ['*', ])
print(tower_builder(2), [' * ', '***'])
print(tower_builder(3), ['  *  ', ' *** ', '*****'])
