def duty_free(price, discount, holiday_cost):
  return int(holiday_cost/((price*discount)/100))

print(duty_free(12, 50, 1000), 166)
print(duty_free(17, 10, 500), 294)