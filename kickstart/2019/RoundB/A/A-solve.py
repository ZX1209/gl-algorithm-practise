import logging
logging.basicConfig(level=logging.DEBUG)


def npMins(a, b):
    """a,b len same
    """
    tmpa = [0] * len(a)
    for i in range(len(a)):
        tmpa[i] = a[i] - b[i]

    return tmpa


def isPalindromes(A):
    odd = 0
    for a in A:
        if a % 2 != 0:  # is odd
            odd += 1
            if odd > 1:
                return False

    return True


def main():
    T = int(input())
    for t in range(T):
        N, Q = list(map(int, input().split()))
        s = input()

        answer = 0

        questions = []
        for q in range(Q):
            questions.append(list(map(int, input().split())))
        tmpS = []
        tmpa = [0] * 26
        tmpS.append(np.array(tmpa))
        for i in range(len(s)):
            tmpa[ord(s[i]) - ord('A')] += 1
            tmpS.append(np.array(tmpa))

        for question in questions:
            tmpa = tmpS[question[1]] - tmpS[question[0] - 1]
            # logging.debug((tmpa))
            if isPalindromes(tmpa):
                # logging.debug((tmpa))
                answer += 1

        print("Case #" + str(t + 1) + ": " + str(answer))


if __name__ == '__main__':
    main()
