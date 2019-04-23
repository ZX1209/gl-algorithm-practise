import logging
logging.basicConfig(level=logging.INFO)


def main():
    T = int(input())

    for t in range(T):
        A,B = list(map(int,input().split(' ')))
        N = int(input())

        while N>0:
            mid = (A+1+B)//2

            print(str(mid))

            response = input()

            if response == "WRONG_ANSWER":
                break
            elif response == "CORRECT":
                break
            elif response == "TOO_SMALL":
                A=mid
            elif response == "TOO_BIG":
                B = mid-1
            N-=1
    return 0
            

if __name__ == '__main__':
    main()
