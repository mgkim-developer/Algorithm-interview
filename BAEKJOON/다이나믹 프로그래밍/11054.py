'''
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN 을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
{10, 20, 30, 25, 20}이 있으면, 30을 기준으로 잡았을 때 바이토닉 수열이 성립된다.
그렇다면, 30을 기준으로 잡을 수 있었던 이유는 무엇일까? 30 왼쪽은 30보다 작으면서 멀어질수록 더 작고, 30오른쪽도 30보다 작으면서 멀어질수록 더 작다.
그렇다면 어떤 수열이 주어졌을 때, 그 수열의 부분 수열 중, 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 방법을 생각해보자.

i)
주어진 배열 arr[]에 대해서
원본 배열에서 LIS 를 구하고,
arr[]을 뒤집어서 LIS를 구하고, 그것을 다시 뒤집으면 arr에 대한 LDS를 구한 값이 된다.
그러면 LIS 배열과 LDS 배열의 같은 인덱스 부분을 더한 값이 가장 큰 값에다가 공통으로 겹치는 인덱스 부분을 고려하여 -1만 해주면 우리가 구하고자하는
가장 긴 바이토닉 부분 수열을 구할 수 있다.
'''
import copy
import plistlib
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
candidate_list = [0 for i in range(n)]

dp_left = [0 for i in range(n)]
dp_right = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp_left[i] < dp_left[j]:
            dp_left[i] = dp_left[j]
    dp_left[i] = dp_left[i] + 1

reverse_arr = copy.deepcopy(arr)
reverse_arr.reverse()   # arr을 뒤집어서 LIS를 구하기 위함

for i in range(n):
    for j in range(i):
        if reverse_arr[i] > reverse_arr[j] and dp_right[i] < dp_right[j]:
            dp_right[i] = dp_right[j]
    dp_right[i] = dp_right[i] + 1

dp_right.reverse()  # arr을 뒤집어서 LIS를 구한 것을 다시 뒤집으면 arr에 대한 LDS임.
result = 0
for i in range(n):
    bitonic =  dp_left[i] + dp_right[i]
    if bitonic > result:
        result = bitonic
result = result - 1 # 공통으로 겹치는 인덱스를 한번 빼줌

print(result)
