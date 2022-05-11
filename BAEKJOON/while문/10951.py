# map함수와 리스트 이용해서 리스트길이가 0일때 while문 종료
import sys
while True:
    a = list(map(int, sys.stdin.readline().split()))
    if len(a) != 0:
        print(a[0]+a[1])
    else:
        break


# try, except 사용해서 오류처리
# import sys
# try:
#     while True:
#         a, b = map(int, sys.stdin.readline().split())
#         print(a+b)
# except:
#     pass
