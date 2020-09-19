print("Enter radius and height")
r = int(input())
h = int(input())
import math
area = math.pi*(r**2)
volume = area*h
print("Volume of the cylinder is {0}".format(volume))