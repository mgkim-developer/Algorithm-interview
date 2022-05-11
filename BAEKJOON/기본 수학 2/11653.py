# 정수 n이 주어졌을 때, 소인수 분해하는 프로그램 작성


n = int(input())

m = 2
while n != 1:
    if n % m == 0:
        print(m)
        n = n / m
    else:
        m = m + 1