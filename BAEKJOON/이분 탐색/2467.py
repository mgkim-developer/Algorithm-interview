# 입력 받기
n = int(input())
solution = (list(map(int,input().split())))
len_solution = len(solution)


def binary_search(array):
    # 두 포인터가 가리키는 수의 합의 절댓값이 작은 것을 저장해서 비교하는데 이용할 것이므로 문제에 따라 가능한 최댓값으로 초기화.
    present_abs = 2000000000

    # sub_abs를 비교해서 저장 현재 두용액의 특성값 합의 절댓값이 sub_abs보다 작다면 각각 result_l, result_r에 저장
    result_l, result_r = 0, 0

    left = 0
    right = len(array) - 1
    result_l, result_r = 0, 0
    while left < right:
        if present_abs >= abs(array[left] + array[right]):
            present_abs = abs(array[left] + array[right])
            result_l = array[left]
            result_r = array[right]
        if array[left] + array[right] >= 0:
            right = right -1
        else:
            left = left + 1

    print(result_l, result_r)

binary_search(solution)