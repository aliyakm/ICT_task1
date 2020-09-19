import math

print("Enter latitude and longitude of two points, respectivelt")
la1 = int(input())
lon1 = int(input())
la2 = int(input())
lon2 = int(input())

pi = math.pi
R = 6371.01

lat1 = (la1*pi)/180
long1 = (lon1*pi)/180
lat2 = (la2*pi)/180
long2 = (lon2*pi)/180

cos_d = math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(long1 - long2)
d = (cos_d)**(-1)

L = d*R

print("The distance is {0} km".format(L))
