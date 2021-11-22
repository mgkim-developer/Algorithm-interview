# 2차원 배열이 주어졌을 때, 해당 배열읠 오른쪽으로 90도 회전시키는 함수
def rotate_a_matrix_by_90_degree_to_right(a):
    row_length = len(a) # (초기화 형태 기준일때 row임)
    column_length = len(a[0]) #(초기화 형태 기준일때 column임)

    res = [[0] * row_length for _ in range(column_length)] # 90도 회전시켜서 초기화

    # 입력된 2차원 배열을 오른쪽으로 90도 회전시키는 방법
    # 입력값의 인덱스를 순서대로, 초기화한 배열의 첫번째 컬럼의 마지막 인덱스부터 마지막 컬럼의 마지막 인덱스까지 순서대로 채운다
    # ex) res[0][row_length -1] 다음 res[1][row_length -1] 다음은 res[2][row_length -1] 이런식으로!!
    for r in range(row_length): #
        for c in range(column_length):
            res[c][row_length - 1- r] = a[r][c]

    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree_to_right(a))

