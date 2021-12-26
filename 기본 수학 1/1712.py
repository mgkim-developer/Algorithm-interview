a, b, c = map(int, input().split())

# print(a) 고정비용
# print(b)  한대당 가변비용
# print(c) 노트북 가격

# 손익분기점 구하기
if c > b :
    result = a // (c-b) + 1
elif c <= b :
    result = -1

print(result)