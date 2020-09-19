print("Please, enter width and length of the field, respectively")

width = int(input())
length = int(input())

area = width*length

area_acre = area/43560

print("The area od the field is {0} acre".format(area_acre))