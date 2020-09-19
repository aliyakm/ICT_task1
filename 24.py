print("Enter the number of days, hours, minutes and seconds")
d = int(input())
h = int(input())
m = int(input())
s = int(input())

total = d*24*60*60 + h*60*60 + m*60 + s
print("The total time is {0} seconds".format(total))