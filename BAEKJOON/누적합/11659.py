'''
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성해야 한다.

입력조건
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
둘째 줄에는 N개의 수가 주어진다. (N <= 1000 인 자연수)
셋째줄부터 M개의 줄에는 합을 구해야하는 구간 i와 j가 주어진다.

i)
일단 구간합 문제로 보여진다.
가장 간단한 구간합 풀이는,
입력받은 수열을 가지고 누적합 배열을 새로 만들어서 갱신한다.
그리고 구간합 구하는 공식인 (i, j)일 때, 누적합배열[j] - 누적합배열[i - 1] 를 수행해서 누적합을 구한다.

코드로 작성해보자.

'''
import sys

# 정답 담을 변수
answer = 0

# 수의 개수 n개, 합을 구해야하는 횟수 m
n, m = map(int,sys.stdin.readline().rstrip().split())
# print(n, m)

# 수열 입력받아서 저장
input_table = list(map(int, sys.stdin.readline().rstrip().split(),))
input_table.insert(0, 0)
# print(input_table)

# 누적합 테이블 생성 및 갱신
prefix_sum = [0 for _ in range(n + 1)]
# print(prefix_sum)

for i in range(1, n + 1):
    if prefix_sum[i - 1] != 0:
        prefix_sum[i] = prefix_sum[i - 1] + input_table[i]
    else:
        prefix_sum[i] = input_table[i]
# print(prefix_sum)

for k in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    # print(i, j)
    answer = prefix_sum[j] - prefix_sum[i - 1]
    print(answer)
