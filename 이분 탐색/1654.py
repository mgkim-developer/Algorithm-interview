import sys

k, n = map(int, input().split())
k_list = []
for i in range(k):
    k_list.append(int(sys.stdin.readline().rstrip()))


# -------------------- binary search 사용 코드 -----------------------
# print(k_list)
k_list.sort()   # 가장 길이가 긴 케이블을 구하기 위해 정렬
# print(k_list)
best_long = k_list[-1]  # 가장 길이가 긴 케이블을 best_long에 저장
# print(best_long)
start = 0
end = best_long

cable_count = 0
while(start <= end):
    cable_count = 0
    mid = (start + end) // 2
    for i in k_list:
        divide_cable = i // mid
        cable_count = cable_count + divide_cable

    if cable_count == n:
        if mid == 0:
            print(1)
        else:
            print(mid)
        break
    elif cable_count < n:
        end = mid - 1
    elif cable_count > n:
        start = mid + 1


# 지금 코드 반례
'''
2 10
1
100

정답은 10
'''



'''
문제를 풀이하며 고민한 과정

2022/03/30
1. 가지고 있는 랜선들의 길이 총합을 구한다.
2. N개의 랜선을 만들어야 하므로, 1번을 N으로 나눈다.
3. 2번길이부터 점차 1씩 줄여가며 최초로 n개의 케이블이 만들어지는 길이를 탐색 시작
시간초과 문제 발생

더 고민해보자..
탐색범위가 100만이라서 이분탐색으로 시간복잡도를 줄여아 할 것 같은데.. 흠..

2022/04/06
생각난 방법,
k_list부분을 sum으로 
그리고, 탐색 부분을 1씩 줄이지 말고 이진탐색 방법론으로 탐색

2022/04/09 
문제의 입력 조건을 보았을 떄, 
랜선의 길이는 231-1보다 작거나 같은 자연수이다.
라는 문구에서 알 수 있듯, 길이 범위가 굉장히 크다.
따라서 이분탐색을 적용해서 풀이해야 하는 문제이다.

# 우선, 가장 길이가 긴 케이블 long_l을 찾는다.
# 0~long_l 의 중간점 mid을 구한다.
# 모든 케이블을 mid으로 나눈 몫의 합 cable_count을 구한다.
# cable_count == N이면 탐색 종료
# cable_count < N이면 end을 mid-1으로 옮기고 다시 중간점 m을 구한다.
# cable_count > N이면 start을 mid+1으로 옮기고 다시 중간점 m을 구한다.
# 이떄의 m을 반환

'''