def Output_the_column_values_of_the_2D_matrix(a):
    row_length = len(a[0])
    column_length = len(a)

    res = [[0] * row_length for _ in range(column_length)]  # 입력값 초기화
    print(res)

    for i in range(column_length):
        for k in range(row_length):
            res[i][k] = a[i][k]

    n = int(input('데이터를 출력하고 싶은 열의 인덱스를 입력하세요(0 ~ column_length-1):'))
    l = [] # 출력하고 싶은 열의 데이터를 담을 빈리스트
    for j in range(column_length):
        l.append(res[j][n])

    return l


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(Output_the_column_values_of_the_2D_matrix(a))