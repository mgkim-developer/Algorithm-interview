a = int(input())
n = 1
while n <= a:
    if n % 10 == 3:
        print('X', end=" ")
    elif n % 10 == 6:
        print('X', end=" ")
    elif n % 10 == 9:
        print('X', end=" ")
    else:
        print(n, end=" ")
    n = n+1
