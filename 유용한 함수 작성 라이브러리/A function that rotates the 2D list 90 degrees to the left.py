def rotate_a_matrix_by_90_degree_to_left(a):
    row_length = len(a) # (초기화 형태 기준일때 row임)
    column_length = len(a[0]) #(초기화 형태 기준일때 column임)

    res = [[0] * row_length for _ in range(column_length)] # 90도 회전시켜서 초기화

    # 입력된 2차원 배열을 왼쪽으로 90도 회전시키는 방법
    for r in range(row_length): # 입력값의 n번째째 열의인덱스를 초기화한 배열의 각 마지막컬럼의 첫번째 인덱스부터 순서대로 채운다
        for c in range(column_length):
            res[column_length -1 - c][r] = a[r][c]

    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree_to_left(a))

