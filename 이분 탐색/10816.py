# upperbound(큰) - lower_bound(같거나 큰)

# 가지고 있는 카드에 적혀있는 정수
n = int(input())
n_list = list(map(int, input().split()))
n_list_alpha = sorted(n_list)

# 가지고 있는 카드에 적혀있는 정수가 몇개인지 구해야할 정수 리스트
m = int(input())
m_list = list(map(int, input().split()))

# --------------이진 탐색 후 count함수 사용하는 방식인데, 시간초과 발생하는 방식임-------------
# result_list = [0] * m

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         # 찾은 경우 중간점 인덱스 반환
#         if array[mid] == target:
#             return mid
#         # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None


# for i in m_list:
#     # 해당 번호가 존재 하는지 확인 후, m_list원소값 순서대로  해당 원소값에 해당하는 원소가 n_list에 있을 때마다 result_list의 해당인덱스의 값을 +1
#     result = binary_search(n_list_alpha, i, 0, n - 1)
#     if result != None:
#         result_list[m_list.index(i)] = n_list_alpha.count(i)
#
# print(n_list_alpha)
#----------------------------------------------------------------------------------

def lower_bound(array, target):

    start, end = 0, len(array)

    while start < end:  # start와 end가 만나는 지점이 target값 이상이 처음 나오는 위치
        # mid = start + (end - start) // 2
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        else:
            end = mid

    return start


def upper_bound(array, target):

    start, end = 0, len(array)

    while start < end:  #start와 end가 만나는 지점이 target값 보다 큰 값이 처음 나오는 위치
        # mid = start + (end - start) // 2
        mid = (start + end) // 2

        if array[mid] <= target:
            start = mid + 1
        else:
            end = mid

    return end

print(n_list_alpha)
print(lower_bound(n_list_alpha, 10))
for i in m_list:
    print(upper_bound(n_list_alpha, i) - lower_bound(n_list_alpha, i), end = ' ')