from collections import Counter
n = int(input())    #원하는 n번째
x = 0 # 현재 숫자
m = 0 # 종말의 숫자가 포함된 횟수
while n != 0:
    x = x+1
    if '666' in str(x): # 만약에 x에 666이 포함되면 m을 +1씩 증가
        m = m+1
    else:
        continue

    if m == n:  #원하는 n번째 종말숫자에 도달하면 종말숫자 출력
        print(x)
        break

