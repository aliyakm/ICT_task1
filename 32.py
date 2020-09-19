a = int(input())
b = int(input())
c = int(input())

num1 = min(a, b)
if num1==a:
    num2 = min(a, c)
    if num2 == a:
        print(a)
        num3 = min(b, c)
        if num3==c:
            print(c)
            print(b)
        else:
            print(b)
            print(c)
        

        