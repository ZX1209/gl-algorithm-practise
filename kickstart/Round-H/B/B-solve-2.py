import logging
logging.basicConfig(level=logging.INFO)

def main():
    T = int(input())

    for t in range(T):
        N = int(input())
        D = [int(c) for c in input()]

        half =N- N//2

        count = 0
        for i in range(half):
            count = max(sum(D[i:i+half]),count)




        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
