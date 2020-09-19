print("Enter initial speed and distance")
vi = int(input())
a = 9.8
d = int(input())
import math
vf = math.sqrt((vi**2) + 2*a*d)
print("Final speed is {0} m/c".format(vf))