print("Enter foot value")
foot = int(input())
print("Enter inch value")
inch = int(input())

cm = foot*12*2.54 + inch*2.54
print("Output: {0} cm".format(cm))