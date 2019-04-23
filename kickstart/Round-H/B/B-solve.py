import logging
logging.basicConfig(level=logging.INFO)

def main():
    T = int(input())

    for t in range(T):
        N = int(input())
        D = [int(c) for c in input()]

        left = 0
        right = len(D)-1
        half = (N//2)

        count = max(sum(D[:N-half]),sum(D[half-N::-1]))

        
        if N%2:
            pass
        else:
            N//=2

        while left<right and N>0:
            if D[left]>=D[right]:
                count-=D[left]
                left+=1
            else:
                count-=D[right]
                right-=1


            N-=1
        
        logging.debug((N,D))

        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
