'''
최소 스패닝 트리

그래프가 주어졌을 때, 그 그래프의 최소 신장 트리 를 구하는 프로그램을 작성하시오.
최소 신장 트리(MST)는 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

- 입력
첫째 줄에는 정점의 개수 v(1 <= v <= 10,000), 간선의 개수 e(1 <= e <= 100,000)가 주어진다.
다음 e개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어짐.
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미.

- 출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력

i)
최소 신장 트리를 구하는 알고리즘인 크루스칼 알고리즘을 적용하여
최소 신장트리의 가중치를 구하면 될 것으로 보임.

'''
import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y, rank):
    rootX = find_parent(parent, x)
    rootY = find_parent(parent, y)

    # 만약 root가 같으면 이미 같은 트리이므로 합치지 않음
    if rootX == rootY:
        return

    # rank가 더 큰 트리에 작은 트리를 붙임
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:   # 만약 rank가 같으면 임의로 rootX트리에 rootY 트리를 붙임
        parent[rootY] = rootX
        rank[rootX] = rank[rootX] + 1

def kruskal():
    total_weight = 0

    # [1] 간선들을 가중치가 작은 순서대로 오름차순 정렬한다.
    edges.sort()

    # [2] 간선들을 하나씩 확인하여 연결한다.
    for weight, v1, v2 in edges:
        if find_parent(parent, v1) != find_parent(parent, v2):  # 같은 집합에 포함되면 union하지 않음
            union_parent(parent, v1, v2, rank)
            total_weight = total_weight + weight

    return total_weight


# 입력 및 실행
v, e = map(int, input().split())

parent = [i for i in range(v + 1)]
rank = [0 for i in range(v + 1)]
edges = []

for i in range(e):
    v1, v2, weight = map(int, sys.stdin.readline().rstrip().split())
    edges.append([weight, v1, v2])

answer = kruskal()
print(answer)


