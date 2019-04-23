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

        for x in range(N-2):
            for y in range(x+1,N-1):
                for z in range(y+1,N):
                    if A[z]==A[x]*A[y] or A[x]==A[z]*A[y] or A[y]==A[x]*A[z]:
                        # logging.debug((A[x],A[y],A[z]))
                        count+=1

        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
