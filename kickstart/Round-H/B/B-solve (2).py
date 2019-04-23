import logging
logging.basicConfig(level=logging.INFO)

def main():
    T = int(input())

    for t in range(T):
        N = int(input())
        D = [int(c) for c in input()]

        left = 0
        right = len(D)-1
        count = sum(D)

        N//=2

        while left<right and N>0:
            if D[left]>=D[right]:
                count-=D[right]
                right-=1
            else:
                count-=D[left]
                left+=1


            N-=1
        
        logging.debug((N,D))

        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
