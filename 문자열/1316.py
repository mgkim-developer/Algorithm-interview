import sys

n = int(input())
a_list = []
for i in range(n):
    a_list.append(list(map(str, sys.stdin.readline().strip())))
not_group_word = 0
for j in range(len(a_list)):
    b = [] #그룹단어인지 확인하기 위해 원소들을 저장하고 확인하가위한 용도
    c = []
    for k in range(len(a_list[j])):
        if a_list[j][k] not in b:
            b.append(a_list[j][k])
        else:
            c.append(a_list[j][k])
    if len(c) != 0:
        not_group_word = not_group_word + 1
    else:
        pass
result = n - not_group_word

print(result)


# 푸는중