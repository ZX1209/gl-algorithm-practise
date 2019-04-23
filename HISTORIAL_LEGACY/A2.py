import logging as log

log.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',
                level=log.INFO)


def A1_solve(N,K,V):
    E=[]
    E.append(sum(V)/N)

    for i in range(1,K+1):
        tmp = [max(val,E[i-1]) for val in V ]
        tmp=sum(tmp)/N
        E.append(tmp)

    return E[K]



T = int(input())

for i in range(T):
    # %% 数据读取
    #N,K
    tmpline=input().split()
    tmpline=list(map(int,tmpline))
    N,K=tmpline

    #V list
    tmpline=input().split()
    tmpline=list(map(int,tmpline))
    V=tmpline

    answer=0

    # %% 数据处理
    answer=A1_solve(N,K,V)


    log.debug('input: '+str(N)+str(K))
    log.debug(V)


    print('Case #'+str(i+1)+': '+str(answer))
