# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[-1]  # 가장 큰 수
second = data[-2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m // (k + 1)) * k
# m이 k+1로 나누어 떨어지지 않을 경우 M을 (K+1)로 나눈 나머지만큼 가장 큰 수가 추가로 더해지므로 이를 고려
count += m % (k + 1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번쨰로 큰 수 더하기

print(result)  # 최종 답안 출력