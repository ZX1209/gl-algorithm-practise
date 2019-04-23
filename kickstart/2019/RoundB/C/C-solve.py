import logging
logging.basicConfig(level=logging.INFO)

from collections import Counter


def Count(i, j, counters, S):
    ans = 0
    tmpCounter = counters[j + 1] - counters[i]

    for v in tmpCounter.values():
        if v <= S:
            ans += v
    return ans


def main():
    T = int(input())
    for t in range(T):
        answer = 0
        N, S = [int(c) for c in input().split()]

        A = input().split()

        logging.debug((N, S, A))

        tmpCounter = Counter()
        counters = [tmpCounter.copy()]
        for i in range(len(A)):
            tmpCounter.update([A[i]])
            counters.append(tmpCounter.copy())

        tmpMax = 0
        for i in range(len(A)):

            for j in range(i + 1, len(A)):
                tmp = Count(i, j, counters, S)
                # logging.debug(tmp)
                if tmp > tmpMax:
                    tmpMax = tmp

        print("Case #" + str(t + 1) + ": " + str(tmpMax))


if __name__ == '__main__':
    main()
