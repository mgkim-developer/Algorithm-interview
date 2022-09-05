# 방법 1
# import sys
#
# # n 입력 받기
# n = int(input())
#
# # 스케줄 입력받기
# schedule = []
# for i in range(n):
#     t, p = map(int, sys.stdin.readline().rstrip().split())
#     schedule.append([t, p])
# # print(schedule)
#
# # dp 테이블 초기화
# d = [0] * (n + 1)
#
# for i in range(n):
#     for j in range(i + schedule[i][0], n + 1):
#         if d[j] <= d[i] + schedule[i][1]:
#             d[j] = d[i] + schedule[i][1]
#
# print(d[-1])


# 방법 2
# import sys
#
# n = int(input())
#
# t_list = []
# p_list = []
# for i in range(n):
#     t, p = map(int, sys.stdin.readline().split())
#     t_list.append(t)
#     p_list.append(p)
#
# max_t = max(t_list)
# dp = [0] * (n+max_t)
#
# for i in range(n):
#     if dp[i] > dp[i + 1]:
#         dp[i + 1] = dp[i]
#     if dp[i + t_list[i]] < dp[i] + p_list[i]:
#         dp[i + t_list[i]] = dp[i] + p_list[i]
#
# print(dp)


# 방법 3 (dp를 뒤에서부터 계산)
import sys

# n 입력 받기
n = int(input())

# 스케줄 입력받기
schedule = [[]]
for i in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    schedule.append([t, p])

# dp 테이블 초기화
d = [0] * (n + 2)

for i in range(n, 0, -1):
    if i + schedule[i][0] > n + 1:
        d[i] = d[i + 1]
    else:
        d[i] = max(d[i + 1], schedule[i][1] + d[i + schedule[i][0]])

print(d[1])