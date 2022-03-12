# 6-12.py 두 배열의 원소 교체

n, k = map(int, input().split())        # N과 K를 입력받기
a = list(map(int, input().split()))     # 배열 A의 모든 원소를 리스트에 원소로 입력받기
b = list(map(int, input().split()))     # 배열 B의 모든 원소를 리스트에 원소로 입력받기

a.sort()                                # 배열 A는 오름차순 정렬 수행
b.sort(reverse = True)                  # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    #  A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i] :
        # 두 원소를 교체(스왑)
        a[i], b[i] = b[i], a[i]
    # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
    else:
        break

# 배열 A의 모든 원소의 합을 출력
print(sum(a))

# 입력 예시
'''
5 3
1 2 5 4 3
5 5 6 6 5
'''