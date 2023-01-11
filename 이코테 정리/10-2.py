# 부모를 찾는 find함수에 경로압축 기법 적용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]