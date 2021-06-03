def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if (mpg*fuel_left) >= distance_to_pump else False


print(zero_fuel(50, 25, 2), True)
print(zero_fuel(100, 50, 1), False)