def rotate_a_matrix_by_180_degree(a):
    row_length = len(a[0]) # (초기화 형태 기준일때 row임)
    column_length = len(a) #(초기화 형태 기준일때 column임)

    res = [[0] * row_length for _ in range(column_length)] # 180도 회전시켜서 초기화

    # 입력을 180도 회전시키는 방법
    for c in range(column_length):  # 입력을 180도 회전시켜서 각인덱스별 원소를 채워줌
        for r in range(row_length):
            res[column_length -1 - c][row_length -1 -r] = a[c][r]

    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_180_degree(a))

