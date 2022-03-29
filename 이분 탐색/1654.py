import sys

k, n = map(int, input().split())
k_list = []
for i in range(k):
    k_list.append(int(sys.stdin.readline().rstrip()))

k_list_sum = 0  # 이미 가지고 있는 랜선들의 길이 총합

for i in (k_list):
    k_list_sum = k_list_sum + i

n_cm =int(k_list_sum / 11)

cable_num = 0
for i in range(n_cm, 0, -1):
    cable_cm = []
    for j in range(len(k_list)):
        cable_cm.append(k_list[j] / i)
    cable_cm_count = 0
    for k in range(len(cable_cm)):
        cable_cm_count = cable_cm_count + cable_cm[k]//1
    if cable_cm_count >= n:
        break
print(i + 1)




'''
문제를 풀이하며 고민한 과정

2021/03/30
1. 가지고 있는 랜선들의 길이 총합을 구한다.
2. N개의 랜선을 만들어야 하므로, 1번을 N으로 나눈다.
3. 2번길이부터 점차 1씩 줄여가며 최초로 n개의 케이블이 만들어지는 길이를 탐색 시작
시간초과 문제 발생

더 고민해보자..
탐색범위가 100만이라서 이분탐색으로 시간복잡도를 줄여아 할 것 같은데.. 흠..




'''