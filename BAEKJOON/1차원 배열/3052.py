l = []
d = []
for i in range(10):
    l.append(int(input()))

for j in range(len(l)):
    d.append(l[j]%42)
d.sort()

c = d[0]
n = 1

for k in range(len(d)):
    if d[k] != c:
        c = d[k]
        n = n+1
    else:
        pass

print(n)