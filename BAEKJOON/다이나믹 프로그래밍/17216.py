import copy
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = copy.deepcopy(arr)

result = 0
for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
