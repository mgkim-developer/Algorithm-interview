'''
n * n 배열을 만든다.
초기화를 해야하는데, 배열에 들어있는 수는 A[i][j] = i×j  이다.
그런데 배열의 인덱스는 1부터 시작한다고 가정함.
A[i][j] = (i+1)×(j+1) 이어야 할 것임 .

1 2 3
2 4 6
3 6 9

'''

n = int(input())
k = int(input())
start = 1
end = k

while start < end:
    count = 0
    mid = (start+end) // 2
    for i in range(1, n+1):
        # mid//i단의 몫이 mid보다 작거나 같은 수의 개수라는 공식을 사용하면,
        # 예를 들어 5보다 작거나 같은 값이 실제로 1단에는 5개가 존재하지만, 만약 문제에서 제시된 N이 3이라면 3개만 존재하는 오류가 발생.
        # 이러한 문제점을 고려하여 n값과 mid//i 값을 비교하여 더 작은 값을 count에 더해줘야한다.
        count = count + (min((mid//i), n))
    # mid보다 작은 수가 k값이랑 같은 경우의 수가 여러개일 가능성이 발생하기 때문에 '찾고자 하는 값과 같거나 큰 수가 있는 첫번째 인덱스를 찾는 'Lower-Bound'를 써야한다.
    if count < k:
        start = mid + 1
    else:
        end = mid
print(start)