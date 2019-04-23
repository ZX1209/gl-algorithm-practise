import logging
logging.basicConfig(level=logging.DEBUG)

def main():
    T = int(input())

    for t in range(T):
        L = int(input())

        N,P = [map(int,input().split(' '))]

        F = []
        for _ in range(P):
            F.append(input())
        count =0

        logging.debug((N,P,F))

        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
