n = int(input())
# print(n)
soldier = list(map(int, input().split()))
# print(soldier)

dp = [1] * n

for i in range(n):
    for j in range(i):
        if soldier[i] < soldier[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(len(soldier) - max(dp))
