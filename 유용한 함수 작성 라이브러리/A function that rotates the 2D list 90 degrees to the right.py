def rotate_a_matrix_by_90_degree_to_right(a):
    row_length = len(a) # (초기화 형태 기준일때 row임)
    column_length = len(a[0]) #(초기화 형태 기준일때 column임)

    res = [[0] * row_length for _ in range(column_length)] # 90도 회전시켜서 초기화

    # 입력된 2차원 배열을 오른쪽으로 90도 회전시키는 방법
    for r in range(row_length): #res의 row의 인덱스를 증가시키며 반복.
        for c in range(column_length):  #res의 컬럼인덱스를 증가시키며 반복. ex) res[0][0] 채우고 res[1][0] 채우고 res[2][0]채움
            res[c][row_length - 1- r] = a[r][c]

    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree_to_right(a))

