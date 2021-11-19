def rotate_a_matrix_by_90_degree(a):
    row_length = len(a) # 회전 시켯을때 기준
    column_length = len(a[0]) #회전 시켯을때 기준

    res = [[0] * row_length for _ in range(column_length)] # 90도 회전시켜서 초기화
    for r in range(row_length): #3번
        for c in range(column_length): # 4번
            res[c][row_length - 1- r] = a[r][c]

    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree(a))