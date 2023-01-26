'''
서로 다른 N개의 자연수의 합이 S라고 한다.
S를 알 때, 자연수 N의 최대값을 구해야 한다.

잘 생각해 보면,
최대한 작은 수를 더해서 S를 만들어야지만 N이 최대가 될 수 있다

n까지 1부터 더해가다가 n보다 큰 값이 나오면, 그 직전의 수가 문제의 정답

S = 10
1
sum 1
result 1
2
sum 3
result 2
3
sum 6
result 3
4
sum 10
result 4
5
sum 15
result 5
'''
import sys

n = int(sys.stdin.readline().rstrip())
sum = 0
result = 0

for i in range(1, n + 1):
    sum = sum + i
    result = i
    if sum > n:
        result = result - 1
        break

print(result)
