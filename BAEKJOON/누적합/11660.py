'''
1, 2, 3, 4
2, 3, 4, 5
3, 4, 5, 6
4, 5, 6, 7
표가 위와 같다면,
2차원 dp table 을 만들고, 누적합을 계산해서 저장해 놓는다.
dp_table =
[[0, 0, 0, 0, 0]
[0, 1, 3, 6, 10],
 [0, 2, 5, 9, 14],
 [0, 3, 7, 12, 18],
 [0, 4, 9, 15, 22]]

그러면 만약에 (x1, y1), (x3, y2) 가 (2, 2), (4, 3)이면 3 + 4 + 4 + 5 + 5 + 6 = 27
dp_table[x1][y2] - dp_table[x1][y1-1] -> 7
+
dp_table[x2][y2] - dp_table[x2][y1-1] -> 9
+
dp_table[x3][y2] - dp_table[x3][y1-1] -> 11

7 + 9 + 11 = 27
규칙을 찾은 듯 하다.

result = 0
for i in range(x1, x3 + 1):
    num = dp_table[i][y2] - dp_talbe[i][y1-1]
    result = result + num
'''
import sys

# 표의 크기 n, 합을 구해야 하는 횟수 M
n, m = map(int, input().split())
# print('n =', n,'m =', m)

# 표를 저장할 리스트 선언
table = [[0] * (n + 1)]

# 표 입력받아서 table에 저장
for i in range(n):
    table_row = list(map(int,sys.stdin.readline().rstrip().split()))
    table_row.insert(0, 0)
    table.append(table_row)
# print("table = ", table)

# dp table 선언
dp_table = [[0] * (n + 1) for _ in range(len(table))]
# print("dp_table = ", dp_table)

# dp_table에 누적합 계산
for i in range(1, len(table)):
    for j in range(1, len(table[1])):
        if dp_table[i][j - 1] != 0:
            dp_table[i][j] = dp_table[i][j - 1] + table[i][j]
        else:
            dp_table[i][j] = table[i][j]

# print("누적합 계산 =", dp_table)

# 합 구하기 m번 수행
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    # print('x1 =', x1, 'y1 =', y1, 'x2 =', x2, 'y2 =', y2)
    result = 0
    for i in range(x1, x2 + 1):
        num = dp_table[i][y2] - dp_table[i][y1 - 1]
        result = result + num
    print(result)