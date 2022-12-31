import sys

# 입력을 저장할 리스트
num_arr = []

a = 0
b = 0
c = 0

INF = int(1e9)
# 한 번 계산된 결과를 메모이제이션(Memoization) 하기 위한 리스트 초기화
d = [[[INF] * (21) for i in range(21)] for j in range(21)]

# 입력받기
while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == -1 and b == -1 and c == -1:
        break
    num_arr.append([a, b, c])

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:  # a, b, c 중에서 0이하가 있으면 return 1
        return 1
    elif a > 20 or b > 20 or c > 20:    # a, b, c중 20보다 큰 값이 있으면 return w(20, 20 , 20)
        return w(20, 20, 20)
    elif d[a][b][c] != INF:     # 값이 존재하면 바로 return d[a][b][c]
        return d[a][b][c]
    elif a < b and b < c:   # a < b < c 이면 return w(a, b, c-1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        d[a][b][c] = w(a, b, c-1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return d[a][b][c]
    else:   # 그 외는 return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        d[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return d[a][b][c]

for i in range(len(num_arr)):
    aa, bb, cc = num_arr[i][0], num_arr[i][1], num_arr[i][2]
    print("w({}, {}, {}) = {}".format(aa, bb, cc, w(aa, bb, cc)))



'''
입력을 받을 건데, 입력의 갯수는 제시되어 있지 않다. 
단, 마지막 입력은 a, b, c가 -1, -1, -1 이 입력된다.
그러면 해당 입력을 기준으로 입력을 마무리 할 것. [완료]

입력을 받았으면 확인해보고, [완료]

문제에서 주어진 함수를 그대로 파이썬으로 작성해보자.
그리고나면 아마 값을 구하는데에 시간이 매우 오래 걸릴 것이다. [완료]

이 문제를 메모이제이션 혹은 DP테이블을 이용하므로서 해결할 수 있을 것으로 예상.
일단 메모이제이션으로 해보자.(탑다운 다이나믹 프로그래밍) 근데 메모이제이션 구조를 어떻게 해야 할지 고민해봐야할듯...
아마도 a, b, c 를 저장해야 하기 때문에 3차원 리스트일 것이다.
그런데, a또는 b 또는 c가 20 보다 큰 것은 w(20, 20, 20)으로 return 해주므로, 3차원 DP를 20까지만 초기화 해놓으면 될 것이다.  [완료]

그리고 로직은, DP에 값이 초기화 한 값과 다르면(값이 존재하면) dp값을 바로 return하고, 값이 존재하지 않으면, dp값을 구하고, 리턴하면 된다. [완료]

DP테이블 초기화는 1e9로 했으므로, 만약 dp값이 1e9라면 값이 존재하지 않는 것으로 판단해야함.   [완료]

주어진 출력조건에 맞게 값을 출력하는 코드를 작성하면 된다.   [완료]
'''