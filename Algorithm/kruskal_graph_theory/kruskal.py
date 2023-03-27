# 특정 원소가 속한 집합을 찾기
import sys


def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, x, y, rank):
    rootX = find_parent(parent, x)
    rootY = find_parent(parent, y)

    # 두 값의 root가 같으면(이미 같은 트리) 연결 X(합치지 않음)
    if rootX == rootY:
        return

    # rank가 큰 트리에 작은 트리를 붙인다.
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:   # 만약 rank가 같다면 임의로 rootX 트리에 rootY 트리를 붙인다.
        parent[rootY] = rootX
        rank[rootX] = rank[rootX]


# 크루스칼
def kruskal():
    total_weight = 0

    # [1] 간선들을 가중치가 적은 순서대로 오름차순 정렬한다.
    edges.sort()

    # [2] 간선들을 하나씩 추출하여 연결한다.
    for weight, v1, v2 in edges:
        if find_parent(parent, v1) != find_parent(parent, v2):  # 같은 집합(트리)에 있는 경우 union하지 않는다. 사이클이 생기기 떄문이다.
            union_parent(parent, v1, v2, rank)
            total_weight = total_weight + weight

    return total_weight

# 노드의 개수와 간선 (union 연산)의 개수 입력받기
v, e = map(int, input().split())

parent = [i for i in range(v + 1)]
rank = [0 for i in range(v + 1)]

edges = []
for i in range(e):
    v1, v2, w = map(int, sys.stdin.readline().rstrip().split())
    edges.append([w, v1, v2])

answer = kruskal()
print(answer)
'''
입력 예시
7 9
1 2 29
1 6 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

출력 예시
159
'''