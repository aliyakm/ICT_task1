print("Enter number of sides and its length")
n = int(input())
s = int(input())
import math
area = n*(s**2)/(4*math.tan(math.pi/n))

print("The area of the regular polygon is {0}".format(area))