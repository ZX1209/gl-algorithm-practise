tmp = input().split()
tmp = tuple(map(int,tmp))
n,na,nb = tmp

tmp = input().split()
tmp = tuple(map(int,tmp))
a = tmp

tmp = input().split()
tmp = tuple(map(int,tmp))
b = tmp

atobResult = (
    (0,0,1,1,0),
    (1,0,0,1,0),
    (0,1,0,0,1),
    (0,0,1,0,1),
    (1,1,0,0,0)
       )

apoint = 0
bpoint =0

for i in range(n):
    tmpa = a[i%na]
    tmpb = b[i%nb]
    apoint+=atobResult[tmpa][tmpb]
    bpoint+=atobResult[tmpb][tmpa]


print(str(apoint)+' '+str(bpoint))


