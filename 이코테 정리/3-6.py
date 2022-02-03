# N, K를 공백으로 구분하여 입력받기
n, k = map(int,input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 떄까지 1씩 뺴기
    target = (n // k) * k
    print(target)
    result = result + (n - target)
    print(result)
    n = target
    print(n)
    # N이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result = result + 1
    print(result)
    n = n//k
    print(n)

# 마지막으로 남은 수에 대하여 1씩 빼기
result = result + (n -1)
print(result)