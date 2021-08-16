a = int(input())
z={}
for i in range(a):
    b = [x for x in input().split()]
    c = int(b[-1])
    q=""
    for i in range(len(b)-1):
         q+=b[i]
    if q not in z:
        z.update({q,c})
print(z)


