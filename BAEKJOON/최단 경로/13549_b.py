'''
BFS를 이용한 다른 풀이

BFS는 인접 노드들을 너비 우선 탐색하면서 최단 경로를 찾는 알고리즘이다.﻿

다만 이 문제는 0과 1의 가중치가 있는 그래프가 대상이기 때문에, BFS를 사용하려면 약간의 변형을 생각해봐야한다.

우선, BFS는 가중치가 없는 그래프에서 가장 먼저 목표 노드를 찾았을 때, 그 때까지의 경로가 최단 경로임이 보장된다.

이 문제에서 너비 우선 탐색했을 때 최단 경로임을 보장하려면, 그래프의 어떤 노드의 인접 노드를 탐색할 때의 가중치가 0인 노드부터 먼저 방문해야 한다.

서로 같은 level에 위치한 노드들 중에서, 가중치가 0인 노드는 가중치를 하나도 늘리지 않고 한 단계 진행할 수 있으므로, 같은 level의 다른 노드로 나아갔을 때와 비교하여 경로의 길이가 줄면 줄었지 최소한 더 늘어나지는 않게된다.

따라서 인접 노드를 탐색할 때 가중치가 0인 노드부터 우선 방문하도록 설계하면, BFS의 '이미 방문했던 노드는 방문하지 않고, 너비를 우선적으로 탐색하는 로직'대로 최단 경로를 찾을 수 있게 된다.
'''
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

# BFS는 한 번 방문한 노드는 다시 방문하지 않음
# 따라서 같은 level에 대하여 인접 노드로의
# 가중치가 0인 2 * x 부터 방문해야 함
def move(x):
    yield (2 * x, 0)
    yield (x - 1, 1)
    yield (x + 1, 1)

def BFS(start):
    graph = [-1] * (100001)
    graph[start] = 0
    q = deque([start])

    while q:
        cnt_x = q.popleft()

        if cnt_x == k:
            return graph[k]

        for node_x, node_time in move(cnt_x):
            cal_time = graph[cnt_x] + node_time
            if 0 <= node_x <= 100000 and graph[node_x] == -1:
                graph[node_x] = cal_time
                q.append(node_x)

print(BFS(n))