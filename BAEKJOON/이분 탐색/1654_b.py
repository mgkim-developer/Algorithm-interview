import sys

k, n = list(map(int, sys.stdin.readline().rstrip().split()))
# print(a, b)

lan_line = []

for i in range(k):
    lan_line.append(int(sys.stdin.readline().rstrip()))

# print(lan_line)

# -------------------- binary search 사용 코드 -----------------------
lan_line.sort()   # 가장 길이가 긴 케이블을 구하기 위해 정렬
# print(k_list)
best_long = lan_line[-1]  # 가장 길이가 긴 케이블을 best_long에 저장
start = 1
end = best_long

while(start <= end):
    cable_count = 0
    mid = (start + end) // 2

    for i in lan_line:
        cable_count = cable_count + (i // mid)

    if cable_count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)