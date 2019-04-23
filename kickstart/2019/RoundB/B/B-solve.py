import logging
logging.basicConfig(level=logging.INFO)


def totalLost(stones, s):
    """totalLost
    """
    if stones == [] or not stones:
        return 0

    total = 0
    for i in range(len(stones)):
        total += min(stones[i][1], s * stones[i][2])
    return total


def main():
    T = int(input())
    for t in range(T):
        answer = 0

        N = int(input())
        stones = []
        for n in range(N):
            tmp = list(map(int, input().split()))
            stones.append(tmp)

        totalSeconds = 0
        totalEnergy = 0

        # stat solving
        while len(stones) > 0:
            minCost = float('inf')
            minIndex = 0
            for i in range(len(stones)):
                tmp = stones[i]
                stones.pop(i)

                tmpTotalLost = totalLost(stones, totalSeconds + tmp[0])
                tmpTotalLost -= max(tmp[1] - totalSeconds * tmp[2], 0)
                logging.debug((tmpTotalLost))

                if tmpTotalLost < minCost:
                    minCost = tmpTotalLost
                    minIndex = i

                stones.insert(i, tmp)

            totalEnergy += max(
                stones[minIndex][1] - totalSeconds * stones[minIndex][2], 0)

            totalSeconds += stones[minIndex][0]
            stones.pop(minIndex)

        print("Case #" + str(t + 1) + ": " + str(totalEnergy))


if __name__ == '__main__':
    main()
