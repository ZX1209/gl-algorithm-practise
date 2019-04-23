import logging
logging.basicConfig(level=logging.INFO)

def contiguousSubArrays(A):
    N = len(A)
    # subArrays
    subAs = []

    for d in range(1,N+1): # contiguous
        for i in range(0,N+1-d): # subArrays
            subAs.append(A[i:i+d])
    return subAs

def dengB(a1,q,n):
    if q==1:
        return a1*n
    return a1*((1-q**n)/(1-q))

def poweri(subA,K):
    l = len(subA)
    tmpsum = 0
    for i in range(l):
        tmpsum += dengB(subA[i],i+1,K)
    return tmpsum




def main():
    T = int(input())

    for t in range(T):
        N,K,x1,y1,C,D,E1,E2,F = list(map(int,input().split(' ')))
        # N is the length of array A
        # K is the number of wakeup calls
        # 
        A = []
        X = [x1]
        Y = [y1]

        summation = 0

        for i in range(N):
            X.append((C * X[i] + D *Y[i] + E1 )%F)
            Y.append((D * X[i] + C *Y[i] + E2 )%F)

            A.append((X[i]+Y[i])%F)

        logging.debug(A)
        logging.debug(X)
        logging.debug(Y)

        # subArrays
        subArrays = contiguousSubArrays(A)

        logging.debug(subArrays)

        for subArray in subArrays:
            for i in range(len(subArray)):
                subArray[i]*=(i+1)

        logging.debug(subArrays)

        for subArray in subArrays:
            summation += poweri(subArray,K)




        print("Case #"+str(t+1)+": "+str(int(summation%1000000007)))


if __name__ == '__main__':
    main()
