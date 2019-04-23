import logging as log
import threading
import numpy as np


log.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',
                level=log.INFO)

threads = []

def A1_solve(N,K,V):
    E=[]
    E.append(sum(V)/N)

    for i in range(1,K+1):
        tmp = [max(val,E[i-1]) for val in V ]
        tmp=sum(tmp)/N
        E.append(tmp)
    print(threading.currentThread().name)
    print(E[K])
    return 0



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

    threads.append(threading.Thread(target=A1_solve,args=(N,K,V,),name='Case #'+str(i+1)+': '))

    threads[-1].start()

    log.debug('input: '+str(N)+str(K))
    log.debug(V)


for t in threads:
    t.join()
    print(t.name+'is finished')


