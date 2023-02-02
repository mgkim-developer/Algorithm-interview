import copy
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for _ in range(n)]

reverse_arr = copy.deepcopy(arr)
reverse_arr.reverse()

for i in range(n):
    for j in range(n):
        if reverse_arr[i] > reverse_arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] = dp[i] + 1

dp.reverse()
print(max(dp))

