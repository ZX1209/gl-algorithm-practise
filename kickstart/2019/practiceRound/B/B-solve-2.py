
T = int(input())

for t in range(T):
    N = int(input())
    D = [int(c) for c in input()]
    total  = sum(D)
    maxS = 0
    l = 0
    r = N-1

    for i in range(N//2):
        if D[l]>D[r]:
            maxS+=D[r]
            r-=1
        else:
            maxS+=D[l]
            l+=1



    print("Case #"+str(t+1)+": "+str(total-maxS))