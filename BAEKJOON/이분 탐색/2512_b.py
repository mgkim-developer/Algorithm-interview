import sys

# n 입력받기
n = int(input())
# print(n)

# 예산 요청 입력 받기
budget_request_og = list(map(int, sys.stdin.readline().rstrip().split()))
# print(budget_request_og)

# 허용된 예산 총량 입력 받기
allow_budget = int(input())
# print(allow_budget)

# 시작점
start = 0
# 끝점
end = max(budget_request_og)

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in budget_request_og:
        if i > mid: # 상한액보다 크면 상한액으로 집행
            total = total + mid
        else:   # 상한액보다 작으면 요청받은 금액 그대로 집행
            total = total + i
    if total <= allow_budget: # 집행금액이 허용예산보다 작거나 같으면
        result = mid
        start = mid + 1
    else: # 집행금액이 허용예산보다 크면
        end = mid - 1

print(result)