a=int(input())
b=int(input())
z=[ ]
g=""
for i in range(b):
    z.append(input())
for i in range(b-1):
    c=0
    for j in range(a):
        if z[i][j] != z[i+1][j]:
            c+=1
            if c > 2:
                print(z[i])
                break 