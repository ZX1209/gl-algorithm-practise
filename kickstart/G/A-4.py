import logging
logging.basicConfig(level=logging.DEBUG)

import math

def C(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))


from collections import Counter
def main():
    T = int(input())

    for t in range(T):
        N = int(input())

        tmp = input().split()
        A = list(map(int,tmp))

        logging.debug((N,A))
        count = 0

        zeros = A.count(0)
        if zeros>=2:
            count+=C(zeros,3)+C(zeros,2)*(N-zeros)

        ones = A.count(1)
        A = [x for  x in A if x>1]
        A.sort()

        if ones>=2:
            c = Counter(A)
            total_repeat = 0
            for num in c.keys():
                if num>=2:
                    total_repeat+=C(num,2)
            count+=C(ones,3)+C(ones,2)*total_repeat
        
        
        N = len(A)
        S = set(A)

        for x in range(N-2):
            for y in range(x+1,N-1): 
                if A[x]*A[y] in S:
                    # logging.debug((A[x],A[y],A[z]))
                    count+=1
                else:
                    break
                    

        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
