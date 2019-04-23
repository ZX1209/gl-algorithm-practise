import logging
logging.basicConfig(level=logging.INFO)


"""
思路
又是重复部分覆盖
"""
def main():
    T = int(input())

    for t in range(T):
        N,P = list(map(int,input().split(' ')))

        F = []
        for _ in range(P):
            F.append(input())
        
        F.sort(key=len)

        l = len(F)
        for i in range(l):
            for j in range(i+1,l):
                if F[j].startswith(F[i]):
                    F[j] = "N"
        
        
        logging.debug((N,P,F))
        count = 2**N;
        for f in F:
            if f !="N":
                count -= 2**(N-len(f))

        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
