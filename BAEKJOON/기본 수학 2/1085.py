"""
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

[조건]
1 <= w, h <= 1000
1 <= x <= w -1
1 <= y <= h-1
x , y, w, h는 정수
"""

x, y, w, h = map(int,input().split())

# print(x, y, w, h)

# 00000000000
# 000000X0000
# 00000000000
# 00000000000

if (w + 1) / 2 > x:
    horizontal_length = x
    if (h + 1) / 2 > y:
        vertical_length = y
    else:
        vertical_length = h - y
else:
    horizontal_length = w - x
    if (h + 1) / 2 > y:
        vertical_length = y
    else:
        vertical_length = h - y


if horizontal_length > vertical_length:
    result = vertical_length
else:
    result = horizontal_length
print(result)


'''
min 함수를 이용한 풀이법

x, y, w, h = map(int, input().split())
print min([x, y, w - x, h - y])
'''