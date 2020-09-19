s = int(input())

d = s//(60*60*24)
s = s - d*24*60*60

h = s//(60**2)
s = s - h*60*60

m = s//60
s = s - m*60

print("{0}:{1}:{2}:{3}".format(d, h, m, s))