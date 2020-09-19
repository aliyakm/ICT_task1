t = int(input())
speed = int(input())

WCI = 13.12 + 0.6215*t - 11.37*(speed**0.16) + 0.3965*t*(speed**0.16)

print(round(WCI))
