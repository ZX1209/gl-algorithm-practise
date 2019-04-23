import logging
logging.basicConfig(level=logging.DEBUG)

import math

from functools import reduce
# 排列组合 C_n^m
def C(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))


def main():

    T = int(input())

    for t in range(T):
        N,M = list(map(int,input().split(' ')))

        count = math.factorial(2*N)
        pre = 0
        tmp = 0
        
        for m in range(M,0,-1):
            pre = tmp
            tmp = math.factorial(M)//math.factorial(M-m)
            tmp*=2**m
            left = 2*N - 2*m

            if left>0:tmp *= reduce(lambda x,y:x*y,[i for i in range(m+1,m+left+1)])

            logging.debug((m,tmp,pre,count))

            
        tmp-=pre*(math.factorial(M)//math.factorial(M-m+1))
        
        count-=tmp

            
        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
