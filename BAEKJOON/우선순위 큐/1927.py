'''
- 문제 요약
최소 힙을 이용하여 다음 연산을 지원하는 프로그램을 작성할 것.
1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

- 입력
첫째 줄에 연산의 개수 N(1 <= N <= 100,000)
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x
    if 정수x가 자연수라면: 배열에 x라는 값을 추가
    elif 정수x가 0이라면: 배열에서 가장 작은 값 출력하고 배열에서 제거
정수 x의 범위는 0 <= x <= 2^31 이다

i) 파이썬의 heapq는 기본적으로 최소힙이다.
이것을 이용하여 로직을 작성하면 될 것 같다.
'''
import heapq
import sys

# 연산의 개수 n
n = int(sys.stdin.readline())

# x를 저장할 힙 배열 선언
heap = []

# x 입력받아서 연산 처리
for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0:              # 만약 힙 배열이 비어 있으면,
            print(0)                    # 조건에 따라 0 출력
        else:                           # 힙이 비어있지 않으면
            tmp = heapq.heappop(heap)   # 가장 작은 값을 뽑아서 배열에서 제거하고
            print(tmp)                  # 뽑은 값을 출력