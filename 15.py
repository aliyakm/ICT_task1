print("Enter feet value")
feet = int(input())

inch = feet*12
yard = feet/3
mile = feet/5280

print("{0} inches, {1} yard, {2} miles".format(inch, yard, mile))