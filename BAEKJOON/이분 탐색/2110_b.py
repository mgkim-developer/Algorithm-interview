n, c = map(int, input().split())   # 집의 개수 n , 공유기의 개수 c
house_pos = []  # 집의 좌표를 저장할 리스트 생성

for i in range(n):  # n개의 집좌표 입력받아서 저장
    a = int(input())
    house_pos.append(a)

# 이분탐색을 위해 집의 좌표를 오름차순으로 정렬
house_pos.sort()

start = 1   # 최소거리
end = int(house_pos[-1]-house_pos[0])   # 최대거리

while start <= end:
    mid =(start + end)//2
    # print('start', start)
    # print("mid", mid)
    # print("end", end)
    count = 1   # 현재 설치되어있는 공유기의 갯수
    set_up = house_pos[0]   # 바로 이전에 공유기가 설치된 곳

    for i in range(1, len(house_pos)):
        if house_pos[i]-set_up >= mid:  # mid(거리) 보다 바로이전에 공유기가 설치된 곳과 현재 설치하려는 곳의 거리가 긴 경우
            set_up = house_pos[i]       # 이전 공유기가 설치된 장소를 저장한 set_up에 공유기를 설치하고 위치를 갱신하여 저장함
            # print("set_up", set_up)
            count = count + 1           # 공유기가 설치된 갯수 +1

    if count >= c:                      # 현재 설치되어 있는 공유기의 갯수가 C보다 많으면,
        result = mid
        start = mid + 1                 # 가능한 길이의 범위를 늘린다. (공유기와 공유기 사이의 거리가 더 커지므로 공유기 설치 갯수를 줄이기 위함)
    else:                               # 현재 설치되어 있는 공유기의 갯수가 C보다 적으면,
        end = mid - 1                   # 가능한 길이의 범위를 줄인다. (공유기와 공유기 사이의 거리가 더 줄어드므로 공유기 설치 갯수를 늘리기 위함)

print(result)