def isOdd(n):
    return n % 2


def DA_solve(num_list, O, D):
    L = 0
    R = 0
    length = len(num_list)
    maxsum = -99999
    sums = [0 for i in range(length)]
    odds = [0 for i in range(length)]

    odds[0] = isOdd(num_list[0])
    sums[0] = num_list[0]
    for i in range(1, length):
        odds[i] = odds[i - 1] + isOdd(num_list[i])
        sums[i] = sums[i - 1] + num_list[i]

    def os(l, r):
        if 0 < l:
            totalodd = odds[r] - odds[l - 1]
            return totalodd
        else:
            return odds[r]

    def ss(l, r):
        if 0 < l:
            totals = sums[r] - sums[l - 1]
            return totals
        else:
            return sums[r]

    for R in range(length):
        if L > R:
            continue

        while os(L, R) > O or ss(L, R) > D:
            L += 1
            if L > R:
                break

        if L > R:
            continue

        tmpsum = ss(L, R)
        if tmpsum > maxsum:
            maxsum = tmpsum

    # while R < length:
    #     while os(L, R) > O:
    #         L += 1
    #         if L>R:
    #             R+=1
    #             break
    #     #then below will be os(L, R) <= O

    #     while ss(L, R) > D:
    #         L += 1
    #         if L>R:
    #             R+=1
    #             break
    #     #then below will be ss(L, R) <= D

    #     tmpsum = ss(L, R)
    #     if tmpsum > maxsum:
    #         maxsum = tmpsum

    #     R += 1

    if maxsum == -99999 or maxsum > D:
        print('IMPOSSIBLE')
    else:
        print(maxsum)

    return 0


def main():
    T = int(input())

    for n in range(T):
        tmp = input().split()
        tmp = list(map(int, tmp))
        N, O, D = tmp

        tmp = input().split()
        tmp = list(map(int, tmp))
        x1, x2, A, B, C, M, L = tmp

        X = [x1, x2]
        S = [x1 + L, x2 + L]

        for i in range(2, N):
            X.append((A * X[i - 1] + B * X[i - 2] + C) % M)
            S.append(X[i] + L)

        print('Case #' + str(n + 1) + ': ', end='')
        DA_solve(tuple(S), O, D)


if __name__ == '__main__':
    main()
