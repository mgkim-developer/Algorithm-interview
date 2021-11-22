# 2차원 배열이 주어졌을 때 원하는 행의 인덱스를 입력하면 해당 인덱스 열의 모든 데이터를 출력하는 함수
def Output_the_row_values_of_the_2D_matrix(a):
    row_length = len(a[0])
    column_length = len(a)

    res = [[0] * row_length for _ in range(column_length)]  # 입력값 초기화

    for i in range(column_length):
        for k in range(row_length):
            res[i][k] = a[i][k]

    n = int(input('데이터를 출력하고 싶은 행의 인덱스를 입력하세요(0 ~ row_length-1):'))
    l = []  # 출력하고 싶은 열의 데이터를 담을 빈리스트
    for j in range(row_length):
        l.append(res[n][j])

    return l


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(Output_the_row_values_of_the_2D_matrix(a))