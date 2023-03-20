# bisect 라이브러리 예제
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))    # 리스트 a에 4를 삽입할 가장 왼쪽 인덱스는 2이다.

print(bisect_right(a, x))   # 리스트 a에 4를 삽입할 가장 오른쪽 인덱스는 4이다.

