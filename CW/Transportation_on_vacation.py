def rental_car_cost(d):
    return (d*40)-50 if d >= 7 else (d*40)-20  if d >= 3 else d*40

print(rental_car_cost(1),40)
print(rental_car_cost(4),140)
print(rental_car_cost(7),230)
print(rental_car_cost(8),270)