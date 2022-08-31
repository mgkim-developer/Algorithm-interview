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

# 정답 담을 리스트
global result
result = [[0, 1]]

# 예산 요청 받은 것을 오름차순 정렬
budget_request_og.sort()
# 요청 받은 예산금액 중 가장 작은 금액
budget_request_min = budget_request_og[0]
# 요청 받은 예산금액 중 가장 큰 금액
budget_request_max = budget_request_og[-1]

# 0부터  높은 금액 사이의 숫자로 된 리스트 생성 (처음에 풀이할 때, 이 범위를 요청 예산중 가장 작은것 ~ 요청 예산중 가장 큰것 으로 설정해서 틀렸었음. 디버깅하며 확인후 수정했음. )
budget_request_num = []
for i in range(0, budget_request_max + 1): # 이거
    budget_request_num.append(i)
budget_request_num_len = len(budget_request_num)
# print(budget_request_num)

# 이분탐색 함수 선언
# 이 함수에서는 요청 받은 예산들중 0부터 가장 큰 금액 사이를 탐색하면서 조건에 맞는 상한액을 찾을 때까지 탐색을 반복함.
def binary_search(budget_request_num, start, end):
    budget_request = budget_request_og[:]
    if start > end:
        return None
    # mid 인덱스는 (start +end // 2)
    mid = (start + end) // 2
    # print("mid",mid)
    # budget_request 리스트를 돌면서
    for i in range(len(budget_request)):
        if budget_request[i] >= budget_request_num[mid]: # 만약에 budget_request[i]가 budget_request_num[mid] 이상인 값은
            # print("budget_request_num[mid]", budget_request_num[mid])
            budget_request[i] = budget_request_num[mid] # budget_request[i]값을 budget_request_num[mid]으로 변환시켜줌
            # print("budget_request[i]", budget_request[i])
    if sum(budget_request) < allow_budget: # 만약에 budget_request 요소값들의 합이 허용 예산 총량 보다 작으면,
        binary_search(budget_request_num, mid + 1, end) # 다시 탐색을 하는데, 탐색 범위를 mid + 1 ~ end 로 지정
        if sum(budget_request) > allow_budget: # 집행할 총 예산 금액이, 허용된 총 예산 금액보다 크면 리턴
            return
        global result
        # 결과 리스트에 sum(budget_request)과 budget_request_num[mid] 를 담기
        if_result = [[sum(budget_request), budget_request_num[mid]]]
        if if_result[0][0] >= result[0][0]:
            result = if_result
    else: # 만약에 budget_request 요소값들의 합이 허용 예산 총량보다 크면 탐색 범위를 start ~ mid - 1 로 지정
        binary_search(budget_request_num, start, mid - 1)
        if sum(budget_request) > allow_budget: # 집행할 총 예산 금액이, 허용된 총 예산 금액보다 크면 리턴
            return
        # 결과 리스트에 sum(budget_request)과 budget_request_num[mid] 를 담기
        else_result = [[sum(budget_request), budget_request_num[mid]]]
        if else_result[0][0] >= result[0][0]:
            result = else_result
        # result.append((sum(budget_request), budget_request_num[mid]))


# 예산 분배 함수 선언
def budget_allocation(n, budget_request):
    if sum(budget_request) <= allow_budget: # 만약에 요청받은 예산들의 합이, 허용된 예산의 총량보다 작으면
        global result
        result = [[1, max(budget_request)]]   # 예산을 요청받은 그대로 집행하고, 가장 큰 예산집행건을 result에 담기
    else: # 만약에 요청받은 예산들의 합이, 허용된 예산의 총량보다 크면
        binary_search(budget_request_num, 0, budget_request_num_len - 1) # 이분탐색 실행. 허용된 예산을 초과하지 않으면서 조건을 만족하는 가장 큰 상한액 찾기


# 함수 실행
budget_allocation(n, budget_request_og)

print(result[0][1])