import logging as log
from bisect import bisect_left

log.basicConfig(level=log.INFO)


T = int(input())

for t in range(T):
    L = int(input())
    Words = input().split()
    S1,S2,N,A,B,C,D = input().split()
    N,A,B,C,D  = list(map(int,(N,A,B,C,D)))
    S = [S1,S2]
    X = [ord(S1),ord(S2)]
    for i in range(2,N):
        X.append(( A * X[i-1] + B * X[i-2] + C )%D)
        S.append(chr(97+X[i]%26))



    print('Case #'+str(t+1)+': '+str(E[K]))
