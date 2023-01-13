'''
수열이 주어지고,
그 수열의 부분 구간합이 가장 큰 것을 구해야 한다.

n과 m이 주어지는데,
n은 전체 수열의 길이 이고, m은 합을 구하기위한 연속적인 날짜의 수이다.

수열이 [3, -2, -4, -9, 0, 3, 7, 13, 8, -3] 이고
n = 10, m = 3 이라면
3 + (-2) + (-4) + (-9) + 0 = -12
(-2) + (-4) + (-9) + 0 + 3 = -12
(-4) + (-9) + 0 + 3 + 7 = -3
(-9) + 0 + 3 + 7 + 13 = 14
0  + 3 + 7 + 13 + 8 = 31
3 + 7 + 13 + 8 + (-3) =  28

그러면 답은 31이 된다.

이거를 좀 빠르고 효율적으로 구하려면 어떻게 해야할까?

i)
일단 누적합 리스트를 작성해보자.

[0, 3, 1, -3, [-12], -12, -9, -2, 11, [19], 16]
m = 5라고 가정하면,

19 - (-12) = 31 -> 답이다.
그러면 그냥 누적합 리스트 갱신한다음, 이중포문 돌리는데,
m칸 차이나는 것까리 빼서
차가 가장 큰 값을 반환하면 될 듯하다.

코드로 구현해보자.

역시.. 이중포문 탓인지 시간초과가 뜬다.

더 효율적인 방법을 생각해 봐야 할 것 같다..

ii)

'''
import sys

# 수열의 길이 n, 합을 구하기 위한 연속적인 날짜의 수 k
n, k = map(int, sys.stdin.readline().rstrip().split())
# print(n, m)

# 수열 입력받기
input_table = list(map(int, sys.stdin.readline().rstrip().split()))
input_table.insert(0, 0)
# print(input_table)

# 누적합 리스트 선언 및 갱신
prefix_sum = [0 for i in range(n + 1)]
# print(prefix_sum)

for i in range(1, n + 1):
    if prefix_sum[i - 1] != 0:
        prefix_sum[i] = prefix_sum[i - 1] + input_table[i]
    else:
        prefix_sum[i] = input_table[i]
# print(prefix_sum)

# 정답 변수 선언 및 초기화
# 정답 변수를 밑에서 tmp와 비교해서 더 큰 값으로 갱신해 주기 때문에, 초기화를 할 때 문제 조건을 잘 읽고 가능한 가장 최소값보다 작은 값으로 초기화 해줘야 한다.
# 그런데 처음에 -101로 초기화 했다가, 또 틀려서 생각해보니, k 길이의 구간합 중 가장 작은 구간합은 (-101) * k 인 것을 파악해서 아래와 같이 초기화 해주었다.
answer = -101 * k

# # (i, j) 라면, j - i가 m 칸 차이나는 것 끼리의 차를 구해서 변수에 저장하고 계속 비교해서 최대값으로 갱신해주기
for j in range(len(prefix_sum) - 1, -1, -1):
    i = j - k
    # print('j =', j, 'i =', i)
    if i < 0:
        pass
    else:
        tmp = prefix_sum[j] - prefix_sum[i]
        if answer < tmp:
            answer = tmp

print(answer)
