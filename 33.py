n = int(input())
sum1 = n*3.49

cost1 = 3.49 - 3.49*0.60
sum2 = n*cost1

print("Regular price for n breads: ", "{0:.2f}".format(sum1))
print("New price for one bread: ", "{0:.2f}".format(cost1))
print("New price for n bread: ", "{0:.2f}".format(sum2))