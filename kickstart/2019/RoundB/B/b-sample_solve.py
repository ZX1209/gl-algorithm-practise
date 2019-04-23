import logging
logging.basicConfig(level=logging.INFO)

tmpAns = 0


def dfsStones(stones, totalSeconds, gain):
    global tmpAns
    if stones == []:
        if gain > tmpAns:
            tmpAns = gain
        return None

    for i in range(len(stones)):
        tmp = stones[i]
        stones.pop(i)

        dfsStones(stones, totalSeconds + tmp[0],
                  gain + max(tmp[1] - totalSeconds * tmp[2], 0))

        stones.insert(i, tmp)


def main():
    global tmpAns
    T = int(input())
    for t in range(T):
        tmpAns = 0

        N = int(input())
        stones = []
        for n in range(N):
            tmp = list(map(int, input().split()))
            stones.append(tmp)
        dfsStones(stones, 0, 0)

        print("Case #" + str(t + 1) + ": " + str(tmpAns))


if __name__ == '__main__':
    main()
