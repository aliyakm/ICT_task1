num = int(input())
n4 = (num%1000)%100%10

n1 = (num - num%1000)/1000

n3 = ((num%1000)%100-n4)/10

n2 = ((num%1000) - num%100)/100

sum = n1 + n2 + n3 + n4

print(round(sum))