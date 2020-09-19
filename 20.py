print("Enter the values of pressure, volume and temoerature")
P = int(input())
V = int(input())
T = int(input())
R = 8.314
n = (P*V)/(R*T)

print("{0} moles".format(n))