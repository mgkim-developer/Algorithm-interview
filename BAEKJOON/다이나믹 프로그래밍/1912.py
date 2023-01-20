'''
n개의 정수로 이루어진 임의의 수열이 주어진다.
이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.

ex) 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어지면,
여기서 정답은 12 + 21이 정답이 된다.

i) dp_table을 만들고, 0번째 인덱스에는 입력받은 테이블의 0번쨰 인덱스 값을 넣어놓는다.
그리고 dp_table의 i 번째 값과 입력받은 테이블의 i + 1 번째인덱스의 값을 합한 값과, 입력받은 숫자의 i + 1번째 값을 비교하여
더 큰 숫자를 dp_table i + 1에 넣어준다.
그리고나서 dp_table에서 가장 큰 값을 출력한다.

구현 해보자.

대부분의 테스트케이스에는 맞으나, 반례를 발견함.

5
-1 -2 -3 -4 -5

디버깅 해본 결과,
인덱스를 맞춰주기 위해 table에 0을 append해준 것이 문제임을 파악함.

만약, 테이블의 모든 값이 음수인 경우, 마지막에 append한 0이 최대값이 되어, 0이 출력되는 문제였다.
따라서, 인덱스를 맞춰주기 위해, 의미없는 값을 넣어주기 위해선, 입력값의 범위를 고려하여, 그 입력값의 하한 범위를 벗어나는 값을 넣어줘야,
구현한 로직과 max가 정상적으로 작동. 그래서 minus_INF 라는 변수를 선언하고, int(-1e9)로 초기화 해줌.

'''
import sys


minus_INF = int(-1e9)

# n 입력받기
n = int(sys.stdin.readline().rstrip())
# 수열 입력받기
table = list(map(int, sys.stdin.readline().rstrip().split()))
# 인덱스 맞춰주기 위해 table에 0을 append
table.append(minus_INF)

# dp_table[i] = max(dp_table[i - 1] + table[i], table[i]) 값을 비교해서 저장하기 위해 dp_table 선언 밎 초기화
dp_table = [0] * (n + 1)
dp_table[0] = table[0]

for i in range(1, n + 1):
    dp_table[i] = max(dp_table[i - 1] + table[i], table[i])

print(max(dp_table))
