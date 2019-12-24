import logging
logging.basicConfig(level=logging.DEBUG)


def bitset(n: int):
    """bitset
    """
    pass


def main():
    T = int(input())
    for t in range(T):
        N, G, M = list(map(int, input().split()))
        Ginfo = []

        for q in range(G):
            Ginfo.append(list(input.split()))

        print("Case #" + str(t + 1) + ": " + str(answer))


if __name__ == '__main__':
    main()
