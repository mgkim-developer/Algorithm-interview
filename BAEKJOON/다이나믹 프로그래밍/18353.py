n = int(input())
# print(n)
soldier = list(map(int, input().split()))
# print(soldier)

dp = [1] * n

for i in range(n):
    for j in range(i):
        if soldier[j] > soldier[i]: # 이 문제에서는 전투력 기준 내림차순 정렬이므로 solider[j] > soldier[i] 이다.
            dp[i] = max(dp[i], dp[j] + 1)
# 이 문제는 LIS(Longest Increasing Subsequence) 알고리즘을 적용하는 문제다.
print(n-max(dp)) # 그러면 dp테이블에는 가장 긴 증가하는 부분 수열 길이가 저장되므로 문제 조건에 따라 (전체길이-가장긴부분수열길이)를 해준 값이 결과다.
