import logging
logging.basicConfig(level=logging.DEBUG)


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
            tmp = ((zeros)*(zeros-1))//2
            count+= tmp*(N-zeros) + ((zeros-2)*(zeros-1))//2

        ones = A.count(1)
        if ones:count+=((ones-2)*(ones-1))//2
        
        
        A = [x for x in A if x>1]
        A.sort()

        if ones:
            c = Counter(A)
            for n in c.values():
                if n>=2:
                    count+=((n-1)*(n))//2



        N = len(A)
        for x in range(N-2):
            if A[x]<=1:
                continue
            for y in range(x+1,N-1):
                for z in range(y+1,N):
                    if A[z]==A[x]*A[y]:
                        # logging.debug((A[x],A[y],A[z]))
                        count+=1
                    elif A[z]>A[x]*A[y]:
                        break


        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
