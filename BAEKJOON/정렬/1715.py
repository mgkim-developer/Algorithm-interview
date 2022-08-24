import heapq

# 항상 가장 작은 크기의 두 카드 묶음을 합쳣을 때 최적의 해 보장.
n = int(input())

heap = []
for i in range(n):
    card_set = int(input())
    heapq.heappush(heap, card_set)

result = 0

# 힙에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기 heapq.heapop 이용
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 heap에 삽입
    sum_card_set = first + second
    result = result + sum_card_set
    heapq.heappush(heap, sum_card_set)

print(result)



# -----------------------------------------리스트와 sort 이용하면 시간초과 나는 코드---------------------------------------------
# import heapq
#
# # 항상 가장 작은 크기의 두 카드 묶음을 합쳣을 때 최적의 해 보장.
# n = int(input())
#
# heap = []
# for i in range(n):
#     card_set = int(input())
#     heapq.heappush(heap, card_set)
#
# result = 0
#
# # 힙에 원소가 1개 남을 때까지
# while len(heap) != 1:
#     # 가장 작은 2개의 카드 묶음 꺼내기 heapq.heapop 이용
#     first = heapq.heappop(heap)
#     second = heapq.heappop(heap)
#     # 카드 묶음을 합쳐서 heap에 삽입
#     sum_card_set = first + second
#     result = result + sum_card_set
#     heapq.heappush(heap, sum_card_set)
#
# print(result)