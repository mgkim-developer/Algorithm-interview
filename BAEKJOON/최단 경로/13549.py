'''
수빈이는 현재 점 N(0 <= N <= 100,000)에 있다.
동생은 점 K(0 <= K <= 100,000)에 있다.

수빈이는 이동을 할 수 있는데,
위치가 X일 때 걷는다면, 1초후에 X - 1 or X + 1의 위치로 이동
순간이동을 한다면, 0초 후에 2*X의 위치로 이동

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초인지 구하는 프로그램 작성할 것.

i)
이 문제는 가중치가 0또는 1인 그래프로 생각할 수 있다.

0부터 10만까지의 노드가 있고, 모든 노드는 0이상 10만 이하의 범위 안에서 -1, +1, 2x의 노드와 간선으로 연결이 되어 있는 그래프이고, 간선의 가중치는 0또는 1이다.
가중치는 모두 0또는 양수이고, 특정 노드에서 특정 노드까지의 최단 경로 가중치를 구하는 것이므로 다익스트라 알고리즘을 적용할 수 있다.

기존의 다익스트라 형태에서 조금 다른 점은, 그래프 간선 정보가 따로 주어지는게 아니라,
현재 노드에 대해 -1, +1, 2x를 인접 노드로 정의하고 순회하면 된다. 이를 위해 제너레이터를 사용한다.

이 때 인접 노드 중 범위를 벗어나는 경우를 걸러줘야 한다.

구현해보자.
'''
import sys
import heapq

INF = int(1e9)
n, k = map(int, sys.stdin.readline().rstrip().split())

# 인접 노드들을 iterable한 값으로 리턴하기 위한 제너레이터 함수
# 코드가 간단해짐
def move(x):
    yield (x - 1, 1)
    yield (x + 1, 1)
    yield (2 * x, 0)

# 다익스트라 알고리즘
def n_to_k(n, k):
    graph = [INF] * (100001)
    graph[n] = 0
    q = [(0, n)]

    while q:
        cnt_time, cnt_x = heapq.heappop(q)

        if cnt_time > graph[cnt_x]:
            continue

        # 0부터 100000까지의 모든 노드들은, 조건 범위 안에서
        # 자신의 -1, +1, *2 의 인접 노드를 가짐
        # 그래서 제너레이터를 통해 직접 인접 노드를 구하여 순회하면 됨
        for node_x, node_time in move(cnt_x):
            cal_time = cnt_time + node_time

            # 인접 노드로 구한 값이 조건 범위 안에 있어야 함
            if 0 <= node_x <= 100000 and cal_time < graph[node_x]:
                graph[node_x] = cal_time
                heapq.heappush(q, (cal_time, node_x))

    return graph[k]

print(n_to_k(n, k))
