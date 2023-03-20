from bisect import bisect_left, bisect_right

# '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 때 유용하다.
def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    print( 'left :', left_index, 'right :', right_index)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))  # 리스트 a에 4는 총 2개 존재한다.

print(count_by_range(a, -1, 3)) # 리스트 a에 -1 ~ 3 사이의 값은 총 6개 존재한다.


