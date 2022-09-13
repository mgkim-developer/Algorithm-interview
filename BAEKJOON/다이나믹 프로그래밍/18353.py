n = int(input())
# print(n)
soldier = list(map(int, input().split()))
soldier.reverse() # LIS 알고리즘을 직관적으로 이용하기 위해 내림차순 입력을 오름차순 입력으로 바꿈
# print(soldier)

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if soldier[j] < soldier[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# 이 문제는 LIS(Longest Increasing Subsequence) 알고리즘을 적용하는 문제다.
print(n-max(dp)) # 그러면 dp테이블에는 가장 긴 감소하는 부분 수열 길이가 저장되므로 문제 조건에 따라 (전체길이-가장긴부분수열길이)를 해준 값이 결과다.