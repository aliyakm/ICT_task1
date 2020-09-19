print("Enter the deposited sum of money")
money = int(input())
percent = 0.10

year1 = money*percent + money
year2 = year1*percent + year1
year3 = year2*percent + year2

print("Year 1: ${0}".format("{0:.2f}".format(year1)))
print("Year 2: ${0}".format("{0:.2f}".format(year2)))
print("Year 3: ${0}".format("{0:.2f}".format(year3)))
