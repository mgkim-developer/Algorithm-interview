import sys

# 점화식에서 이전값을 사용해야하는데, 첫번째 값의 이전값 사용을 위해 공백 추가
str1 = ' ' + sys.stdin.readline().rstrip()
str2 = ' ' + sys.stdin.readline().rstrip()
# print(str1)
# print(str2)

dp = [[0] * len(str2) for i in range(len(str1))]

print(dp)

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]: # 만약에 str1[i]와 str[j]가 같으면
            dp[i][j] = dp[i-1][j-1] + 1 # 이전 DP 테이블에 저장한 LCS 길이+1 를 해준다.
        else: # 각 문자열의 마지막 글자가 다를 때에는
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 각 문자열의 마지막 글자들이 따로 한 글자씩 추가되었을 때의 각 경우중 LCS가 큰 값을 DP테이블에 저장.

# print(dp)
print(dp[-1][-1])