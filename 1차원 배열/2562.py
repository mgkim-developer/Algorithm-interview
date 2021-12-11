a = []
for i in range(9):
    a.append(int(input()))

b = 0
for i in range(len(a)):
    if max(a) == a[i]:
        b = i+1
    else:
        pass

print(max(a))
print(b)
