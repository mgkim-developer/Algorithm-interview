# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 100
dp[1] = 1
dp[2] = 1
n = 99

# 피보나치 수열을 반복문으로 구현(Bottom-Up DP)
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
