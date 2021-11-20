def rotate_a_matrix_by_180_degree(a):
    row_length = len(a[0]) # (초기화 형태 기준일때 row임)
    column_length = len(a) #(초기화 형태 기준일때 column임)

    res = [[0] * row_length for _ in range(column_length)] # 180도 회전시켜서 초기화
    for i in range(column_length):  # 초기화한 곳에 각인덱스별 원소를 채워줌
        for k in range(row_length):
            res[i][k] = a[i][k]
        res[i].reverse()        # reverse를 이용하서 180도 회전시킨 값과 동일하게 만들어줌
    res.reverse()
    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_180_degree(a))

