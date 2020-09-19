s1 = int(input())
s2 = int(input())
s3 = int(input())
import math 
p = (s1+s2+s3)*0.5
area =math.sqrt(p*(p-s1)*(p-s2)*(p-s3))    

print("Area of thr triangle is {0}".format(area))