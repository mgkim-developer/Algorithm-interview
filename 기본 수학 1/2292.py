'''
1 에서 출발
2   [2, 3, 4, 5, 6, 7] 총 6개
3   [8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19] 총 12개
4   [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37] 총 18개
5   [38~61] 총 24개
'''

a = int(input())

i = 0
n = 0
number = 0

while n < 1000000000:
    n = n + 6
    number = number + n
    i = i+1
    if a <= number+1:
        result = i + 1
        break
    else:
        pass

print(result)
