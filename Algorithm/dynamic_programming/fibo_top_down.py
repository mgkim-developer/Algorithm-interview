# 메모이제이션 하기 위한 리스트 초기화
memoization = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (Top-down)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있으면 그대로 반환
    if memoization[x] != 0:
        return memoization[x]
    # 계산한 적 없으면 점화식에 따라 피보나치 결과 반환
    memoization[x] = fibo(x - 1) + fibo(x - 2)
    return memoization[x]

print(fibo(6))
