'''
M * N  크기의 보드가 있는데, 어떤 정사각형은 검은색으로 칠해져있고, 나머지는 휜색으로 칠해져있음.
이 보드를 잘라서 K * K 크기의 체스판으로 만들려고함.

정상적인 체스판은 검은색과 휜색이 번갈아서 칠해져 있어야 함.
구체적으로, 각 칸이 검은색과 휜색 중 하나로 칠해져 있으면서,
변을 공유하는 두개의 사각형은 다른 색으로 칠해져 있어야 함.
이 정의를 따르면, 체스판을 색칠하는 경우는 두 가지 뿐이다.
1. 맨 왼쪽 위 칸이 휜색인 경우,
2. 맨 왼쪽 위 칸이 검은색인 경우

보드가 체스판 처럼 칠해져 있다는 보장이 없어서,
M * N 크기의 보드를 K * K 로 자른 후, 몇개의 정사각형을 다시 칠해서 체스판으로 만들 것임.

다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성 할 것.

입력은
첫째 줄에 N(세로)행, M(가로)열, K
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어짐. (B는 검은색, W는 휜색)
1 <= N, M <= 2000
1 <= K <= min(N, M)


i)
간단한 예제를 먼저 시뮬레이션 해보자.
4 4 3
BBBB
BBBB
BBBW
BBWB
이면,
3 * 3 크기로 자른 후, 가장 적은 칸을 칠해서 체스판을 만들 수 있는 것의 칸 개수를 구해야 한다.
그러면, 일단은 4 * 4 보드를 3 * 3으로 자를 수 있는 경우를 구하고,
각 경우에 대해서 좌측 상단이 B일 때와, W일 때로 나누어
몇개를 다시 색칠해야 하는지 구해서 비교해볼 수 있을 것이다.

그런데, 문득 들은 생각인데,
처음부터 3 * 3 으로 자를 수 있는 경우를 구하기 전에
입력받은 보드를 아예 좌측 상단이 B인 것과, 좌측 상단이 W인 것으로 나누어 테이블을 만들고,

좌측 상단이 B 인것
BWBW
WBWB
BWBW
WBWB

좌측 상단이 W 인것
WBWB
BWBW
WBWB
BWBW

이렇게 있으면,
누적합 테이블을 b누적합테이블, w누적합 테이블 이렇게 두개 만들어서
정상적인 체스판과 다른 부분의 개수를 카운트해서 갱신하고,
거기서 3 * 3 크기에 해당하는 부분의 누적합을 구해서 가장 작은 부분을 반환하면 되지 않을까?

코드로 구현해보자.

일단 시간초과 난다.

ii)
처음 생각한 기본 로직은 맞는 것 같음.
그러면 이제 시간복잡도, 공간복잡도 등을 고려해서
'''

import sys

# n, m, k 입력받기
n, m, k = map(int, sys.stdin.readline().rstrip().split())
# 보드 입력받아서 저장하기
board = []
for i in range(n):
    str = list(sys.stdin.readline().rstrip())
    board.append(str)
# print(board)

# 왼쪽 상단이 B라고 가정한 누적합 리스트
b_prefix_sum = [[0] * (m + 1) for _ in range(n)]
# print(b_prefix_sum)
# 왼쪽 상단이 W라고 가정한 누적합 리스트
w_prefix_sum = [[0] * (m + 1) for _ in range(n)]
# print(w_prefix_sum)

# n * m 크기의 정상적인 체스판 생성
# 좌측 상단이 B인 것으로 하나만 생성하고, W인 것은 조건을 반대로 넣어서 비교 할 것임.
good_board = [[0] * m for _ in range(n)]
for i in range(len(good_board)):
    for j in range(len(good_board[0])):
        if i % 2 == 0:
            if j % 2 == 0:
                good_board[i][j] = 'B'
            else:
                good_board[i][j] = 'W'
        else:
            if j % 2 == 0:
                good_board[i][j] = 'W'
            else:
                good_board[i][j] = 'B'
# print(good_board)

for i in range(n):
    for j in range(m):
        # 좌측 상단이 B라고 가정한 누적합 리스트 갱신 (정상 체스판과 다른 갯수를 갱신 할 것임)
        if good_board[i][j] != board[i][j]:
            if b_prefix_sum[i][j] == 0:
                b_prefix_sum[i][j + 1] = 1
            else:
                b_prefix_sum[i][j + 1] = b_prefix_sum[i][j] + 1
        else:
            b_prefix_sum[i][j + 1] = b_prefix_sum[i][j]
        # 좌측 상단이 W라고 가정한 누적합 리스트 갱신 (정상 체스판과 다른 갯수를 갱신 할 것임)
        if good_board[i][j] == board[i][j]:
            if w_prefix_sum[i][j] == 0:
                w_prefix_sum[i][j + 1] = 1
            else:
                w_prefix_sum[i][j + 1] = w_prefix_sum[i][j] + 1
        else:
            w_prefix_sum[i][j + 1] = w_prefix_sum[i][j]
# print(b_prefix_sum)
# print(w_prefix_sum)

# 정상 체스판과 다른 갯수를 저장할 변수
result = int(1e9)

# k * k 크기로 자른다고 가정하고, 누적합 리스트를 이용하여 정상체스판과 색이 다른칸 개수 카운트하기
for j in range(len(b_prefix_sum[0]) - 1, -1, -1):
    i = j - k
    b_tmp = 0
    w_tmp = 0
    a = 0
    if i < 0:
        pass
    else:
        # print(i, j)
        for y in range(len(b_prefix_sum)):
            if a + (k - 1) < len(b_prefix_sum) and y + (k - 1) <= len(b_prefix_sum):
                # print(a)
                for x in range(a, a + k):
                    b_tmp = b_tmp + b_prefix_sum[x][j] - b_prefix_sum[x][i]
                    w_tmp = w_tmp + w_prefix_sum[x][j] - w_prefix_sum[x][i]
                a = a + 1
                tmp = min(b_tmp, w_tmp)
                b_tmp = 0
                w_tmp = 0
                if tmp < result:
                    result = tmp

print(result)