n = int(input())
num_n = list(map(int, input().split()))
num_n.sort()
# print(num_n)
m = int(input())
num_m = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

for i in num_m:
    # 해당 번호가 존재하는지 확인
    result = binary_search(num_n, i, 0, n - 1)
    if result != None:
        print('1')
    else:
        print('0')