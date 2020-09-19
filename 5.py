print("Please choose: one liter or less = 1, more than 1 liter = 2")

volume = int(input())

print("Please write the number of drink containers")

number = int(input())

if volume == 1:
    deposit = number*0.10
    print("Your deposit is ${0}".format(deposit))
elif volume == 2:
    deposit = number*0.25
    print("your deposit is ${}".format(deposit))
else:
    print("You chose wrong number for volume type")
