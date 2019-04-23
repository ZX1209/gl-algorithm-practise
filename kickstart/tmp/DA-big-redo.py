def addtomultiset(l,n):
    isserted = 0
    for i in range(len(l)):
        if n<l[i]:
            l.insert(i,n)
            isserted = 1
            break
    if not isserted:
        l.append(n)


def isOdd(n):
    return n % 2


def DA_solve(num_list, O, D):
    L = 0
    length = len(num_list)
    maxsum = -99999

    sums = [0 for i in range(length)]
    sums[0] = num_list[0]
    for i in range(1, length):
        sums[i] = sums[i - 1] + num_list[i]

    sums = tuple(sums)

    s = []
    cnt_odd = 0
    for R in range(0, length-1):
        addtomultiset(s,sums[R])
        cnt_odd += num_list[R+1] & 1

        while cnt_odd > O:
            s.remove(sums[L])
            cnt_odd -= num_list[L+1] & 1
            L += 1

        for index in range(len(s)):
            if s[index] >= sums[R+1] - D:
                maxsum = max(maxsum, sums[R+1] - s[index])
                break

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