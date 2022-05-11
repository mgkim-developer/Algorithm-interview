a = input() # 입력 받기=
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=' ,'z=']

for i in croatia:
    a = a.replace(i, '*')
print(len(a))