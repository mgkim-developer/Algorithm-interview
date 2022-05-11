# a = int(input())
# l = [] # 빈 리스트
# m = 0 # 분모
# s = 0 # 분자
#
# for i in range(1, a+1):
#     sub_l = []
#     for j in range(1, i+1):
#         s = i-j+1
#         m = j
#         sub_l.append('{}/{}'.format(s, m))
#     if i % 2 == 0:
#         sub_l.reverse()
#         for k in range(len(sub_l)):
#             l.append(sub_l[k])
#     else:
#         for k in range(len(sub_l)):
#             l.append(sub_l[k])
# print(l[a-1])
# -----------------------------메모리 초과로 다시 생각하여 새롭게 코딩 ----------------------------

a = int(input())
l = []
n = 0   # 사선 라인
max_num = 0 # 입력된 숫자가 속한 라인에서 가장 큰 숫자
while a > max_num:
    n = n + 1
    max_num = max_num+n

gap = max_num-a

if n % 2 == 0:
    s = n-gap
    m = gap+1
else:
    s = gap+1
    m = n-gap
print('{}/{}'.format(s, m))