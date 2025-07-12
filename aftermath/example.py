#matrix multiplication

a=[[1, 2], [3, 4]]
b=[[1, 2], [3, 4]]

an=len(a)
bn=len(b)
am=len(a[0])

final=[]

for i in range(an):
    row=[]
    for j in range(am):
        tot=0
        for k in range(am):
            tot+=a[i][k]*b[k][j]
        row.append(tot)
    final.append(row)

print(final)