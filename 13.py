print('Enter a number between 0-99:')
n = int(input())
print(n//25, "Quarters")
n = n%25
print(n//10, "Dimes")
n = n%10
print(n//5, "Nickles")
n = n%5
print(n//1, "Pennies")