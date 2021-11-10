# while과 if를 함께 사용한 방법
# a = 1
# while a != 0:
#     a = int(input())
#     if a != 0:
#         print(a)

# bool을 사용한 방법 0 은 False이기 떄문
a = 1
while a != 0:
    a = int(input())
    if bool(a) == True:
        print(a)
