n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = trees[-1]

while start <= end:
    mid = (start+end)//2
    cut_len = 0

    for i in trees:
        if i < mid:
            pass
        else:
            cut_len = cut_len+(i-mid)

    if cut_len < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)