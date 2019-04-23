import logging
logging.basicConfig(level=logging.DEBUG)

def main():
    T = int(input())

    for t in range(T):
        tmp = list(map(int,input().split()))
        N,Q = tmp

        tmp = list(map(int,input().split()))
        X1,X2,A,B,C,M = tmp
        X = [X1,X2]
        for i in range(2,N):
            X.append((A * X[i-1]+ B*X[i-2]+C)%M)

        tmp = list(map(int,input().split()))
        Y1,Y2,A,B,C,M = tmp
        Y = [Y1,Y2]
        for i in range(2,N):
            Y.append((A * Y[i-1]+ B*Y[i-2]+C)%M)
        
        tmp = list(map(int,input().split()))
        Z1,Z2,A,B,C,M = tmp
        Z = [Z1,Z2]
        for i in range(2,Q):
            Z.append((A * Z[i-1]+ B*Z[i-2]+C)%M)
        
        L = []
        for i in range(N):
            L.append(min(X[i],Y[i])+1)
        R = []
        for i in range(N):
            R.append(max(X[i],Y[i])+1)
        K = []
        for i in range(Q):
            K.append(Z[i]+1)
        
        S = 0
        sorces = []

        for i in range(N):
            sorces.extend(list(range(L[i],R[i]+1)))
        
        sorces.sort(reverse=True)

        for i in range(Q):
            try:
                S+=(i+1)*sorces[K[i]-1]
            except:
                continue
                


        logging.debug((X,Y,Z,L,R,K))

        print("Case #"+str(t+1)+": "+str(S))


if __name__ == '__main__':
    main()
