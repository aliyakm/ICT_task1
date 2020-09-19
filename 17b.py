print("Mass in grams:")
m = int(input())
print("Temperature in Celsius:")
dt = int(input())
q = m * dt * 4.186
print("The total energy in Joules: %f" %q)
c = (q * 8.9) / 3600000
price = c / 100
print("The total cost needed to be payed is %f dollars" %price)
