# union-by-rank 최적화 적용 union 함수
def union_parent(parent, x, y, rank):
    rootX = find_parent(parent, x)
    rootY = find_parent(parent, y)

    # 두 값의 root가 같으면(이미 같은 트리) 연결 X(합치지 않음)
    if rootX == rootY:
        return

    # union-by-rank 최적화
    # rank가 더 큰 트리에 작은 트리를 붙인다.
    # 즉, 높이가 더 높은 쪽을 root로 한다.
    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else: # 만약 rank가 같다면 임의로 rootX 트리에 rootY 트리를 붙인다.
        parent[rootY] = rootX
        rank[rootX] = rank[rootX] + 1   # rootX 트리의 높이를 + 1

# -------------------------------------------------------
# 경로압축 기법 적용한 find 함수
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]