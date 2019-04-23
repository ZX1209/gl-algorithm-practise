from collections import Counter


def isOdd(n):
    return n % 2

def sortl(ls):
    sums = Counter()
    tmpl = []
    for i in range(len(ls)):
        sums[i] = sum(ls[i])

    for i, j in sums.most_common():
        tmpl.append(ls[i])

    return tmpl

def rate(lhu,lla):
    win = 0
    total = 0
    for hu in lhu:
        for la in lla:
            total += 1
            if hu>la:
                win+=1

    return wi


def dfs()

# la win >=
# hu win >
def solve_EC(N, hu, la):
    lla = [sum(la[i:i+N]) for i in range(N)]

    win = 0
    lla.sort()
    hu.sort()

    while 


    for i in range(3*N):
        if hu[i] > la[i]:
            win += 1
    return win/(3*N)


def main():
    T = int(input())

    for t in range(T):
        tmp = input().split()
        tmp = list(map(int, tmp))
        N, = tmp

        tmp = input().split()
        tmp = list(map(int, tmp))
        hu = tmp

        tmp = input().split()
        tmp = list(map(int, tmp))
        la = tmp
        print('Case #' + str(t + 1) + ': ', end='')
        print(solve_EC(N, hu, la))


if __name__ == '__main__':
    main()
