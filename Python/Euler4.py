b = []
for j in range(100,1000):
    for k in range(100,1000):
        if list(str(j*k)) == list(reversed(str(j*k))):
            b.append((j,k))

c=[0]
for (j,k) in b:
    if j*k > c[0]:
        c[0]=j*k
print(c[0])  