def rotate_a_matrix_by_90_degree_to_left(a):
    row_length = len(a) # (초기화 형태 기준일때 row임)
    column_length = len(a[0]) #(초기화 형태 기준일때 column임)

    res = [[0] * row_length for _ in range(column_length)] # 90도 회전시켜서 초기화
    for r in range(row_length): #res의 row의 인덱스를 증가시키며 반복.
        for c in range(column_length):  #res의 컬럼인덱스를 증가시키며 반복. ex) res[0][0] 채우고 res[1][0] 채우고 res[2][0]채움
            res[c][row_length - 1- r] = a[r][c]
    # 여기까지는 오른쪽으로 90도 회전시킬 떄랑 같음.
    for k in range(column_length):  # 오른쪽으로 90도 회전시킨 결과를 reverse를 이용해서 왼쪽으로 90도 회전시킨 것과 동일하게 바꿔줄 수 있음.
        res[k].reverse()

    res.reverse()
    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree_to_left(a))

