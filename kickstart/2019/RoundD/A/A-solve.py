import logging
logging.basicConfig(level=logging.DEBUG)


def bitset(n: int):
    """bitset
    """
    pass


def main():
    T = int(input())
    for t in range(T):
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))

        for q in range(Q):
            P, V = list(map(int, input().split()))

        print("Case #" + str(t + 1) + ": " + str(answer))


if __name__ == '__main__':
    main()
