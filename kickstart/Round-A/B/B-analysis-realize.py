import logging as log
from bisect import bisect_left

log.basicConfig(level=log.INFO)


T = int(input())

for t in range(T):
    N,K = list(map(int,input().split()))
    V = list(map(int,input().split()))
    V.sort()
    S = V.copy()
    for i in range(1,N):
        S[i]+=S[i-1]

    E = [0 for _ in range(K+1)]
    E[0] = S[N-1]/N

    for i in range(1,K+1):
        # 返回,V中最小的大于等于E[i-1] 的数的索引
        lowerIndex = bisect_left(V,E[i-1])
        # lowerIndex 之前的都是小于E[i-1] 的

        # log.info((lowerIndex,N,i))
        if lowerIndex<=0:
            E[i] =  E[0]
        elif lowerIndex>=N:
            E[i] =  E[i-1]
        else:
            E[i] =  ((E[i-1] * (lowerIndex)) + S[N-1]-S[lowerIndex-1])/N


    

    print('Case #'+str(t+1)+': '+str(E[K]))
