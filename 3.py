print("Please, choose the appropriate unit: feet = 1, meter = 2.")
unit = int(input())

print("Please, enter width and length of the room, respectively")

width = float(input())
length = float(input())

if unit == 1:
    area = width*length
    result = "The area of the room is {0} feets"
    print(result.format(area))
elif unit == 2:
    area = width*length
    result = "The area of the room is {0} meters"
    print(result.format(area))
else:
    print("You didn't write a correct number of unit")
