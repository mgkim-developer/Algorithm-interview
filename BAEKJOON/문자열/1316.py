import sys

n = int(input())
a_list = []
for i in range(n):
    a_list.append(list(map(str, sys.stdin.readline().strip())))
# print(n)
# print(a_list)
# print(len(a_list))

not_group_word = 0
for j in range(len(a_list)):
    a = []
    b = []
    for k in range(len(a_list[j])):
        # print(a_list[j][k])

        if a_list[j][k] not in a:
            a.append(a_list[j][k])
            # print(a)
        else:
            if a[-1] == a_list[j][k]:
                a.append(a_list[j][k])
                pass
            else:
                if a_list[j][k] not in b:
                    not_group_word = not_group_word + 1
                    b.append(a_list[j][k])
                    # print(b)
                    break
                else:
                    pass


result = n - not_group_word
print(result)