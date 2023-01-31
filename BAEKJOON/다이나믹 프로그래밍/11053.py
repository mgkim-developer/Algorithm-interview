'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성 해야한다.
ex) A = {10, 20, 10, 30, 20, 50}인 경우, LIS(Longest Increasing Subsequence)는
{10, 20, 30, 50} 이고, 길이는 4이다.

입력은 수열의 크기 N
둘째줄에는 수열을 이루고 있는 숫자들이 공백을 구분으로 주어진다.

i)
7
1000 10 20 10 30 20 50
이 입력에 대해서 생각을 해보자.

dp_table을 만들고,
arr과 인덱스를 맞춰서 dp[i]에는 arr[i] 숫자까지의 최장 증가 부분 수열 개수 저장할 것이다.

arr[0]인 1000을 먼저 보면, 앞에 아무것도 없으므로, dp[0]에 dp[0] + 1을 저장 한다. - > dp[0] = 1

arr[1]인 10을 보면, 앞에는 1000이 있다. 1000 < arr[1]은 false이므로  dp[1] = dp[1] + 1 을 한다. -> dp[1] = 1

arr[2]인 20을 보면, 앞에는 1000과 10이 있다. 1000<arr[2]은 false다. 10 < arr[2]은 true이고, dp[2] < dp[1]는 true 이므로 dp[2] = dp[1]을 하고, 1000과 10을 다 확인 했으므로 dp[2] = dp[2] + 1을 해준다. -> dp[2] = 2

arr[3]인 10을 보면, 앞에는 1000과 10, 20이 있다. 1000<arr[3]은 false다. 10 < arr[3]는 false다. 20 < arr[3]은 false다. 1000과 10과 20을 다 확인했으므로 dp[2] = dp[2] + 1을 해준다. -> dp[3] = 1

arr[4]인 30을 보면, 앞에는 1000과, 10, 20, 10 이 있다. 1000<arr[4]는 false다 10 < arr[4]는 true 이고, dp[4] < dp[1] 는 true이므로 dp[4] = dp[1] 을 한다. 그리고  20 < arr[4] 는 trye이고, dp[4] < dp[2] 는 true이므로 dp[4] = dp[2] 를 해준다.  10 < arr[4]는 true이고, dp[4] < dp[3] 은 false이다. 다 확인했으므로, dp[4] = do[4] + 1 -> dp[4] = 3

arr[5]인 20을 보면, 앞에는 1000과, 10, 20, 10, 30이 있다. 1000 < arr[5]는 false다. 10 < arr[5]는 true이고, dp[5] < dp[1]은 true 이므로 dp[5] = dp[1]을 한다. 그리고 20 < arr[5]는 false이다. 10 < arr[5]는 true이고, dp[5] < dp[1]은 false이다. 30 < arr[5]는 false이다. 다 확인했으므로, dp[5] = dp[5] + 1 -> dp[5] = 2

arr[6]인 50을 보면, 앞에는 1000과 10, 20, 10, 30, 20이 있다. 1000< arr[6]은 false다. 10 < arr[6]은 true이고, d[6] < dp[1]은 ture 이므로 d[6] = dp[1]을 한다. 그리고 20 < arr[5]는 ture 이고, dp[6] < dp[2]는 이므로 dp[6] = dp[2]를 한다. 10 < arr[6]은 true이고, dp[6] < dp[3]은 false이다. 30 < arr[6]은 true이고, dp[6] < dp[4] 은 true이므로 dp[6] = dp[4]를 해준다. 20 < arr[6]은 true이고, dp[6] < dp[5]는 false이다. 다 확인했으므로, dp[6] = dp[6] + 1 -> 4

최종 dp_table은 [1, 1, 2, 1, 3, 2, 4] 이다. 여기서 max값을 뽑아주면 구하고자하는 답이 된다.


'''

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] = dp[i] + 1

print(max(dp))