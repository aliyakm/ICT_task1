print("Enter the cost of the dish")
cost = int(input())

tip = cost*0.18

tax = cost*0.15

final_cost = tip + tax + cost

print("{0:.2f}".format(final_cost))