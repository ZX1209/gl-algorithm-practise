# EB.py

# 比赛分析
# 概述|问题A |问题B |问题C.
# 对于Small数据集，只有2P种不同的选项组合可用。由于P最多为10，因此只有1024种可能的组合。采取给出最少错误的组合，这是不被禁止的。

# 对于Large数据集，首先要注意最多有100个禁用组合。一种方法是生成101个组合，这些组合引起最少的投诉并采取最好的不被禁止的组合（至少有一个组合在前101中不被禁止）。

# 要生成这些组合，首先要注意的是，就您将获得的投诉数量而言，每个选项都可以单独考虑。为了以后帮助我们，对每个选项进行预处理，如果我们要使用该选项获得奶茶而没有它，我们会得到多少投诉。我们现在将一次选择最佳组合。

# 让Tk表示当我们仅考虑前k个选项时产生最少投诉的前101个组合，表示为二进制字符串（任意绞刑）。关键的想法是要注意Tk + 1中的每个组合都有一个Tk组合作为前缀。

# 这很容易通过矛盾表现出来。从Tk + 1中取任何字符串S并删除最后一位以获得前缀S'。假设S'不是Tk的矛盾。在Tk中取任何字符串并附加删除的位将给出一个组合，该组合严格地产生（在考虑抢七时）投诉。这提供了101个字符串，产生较少的投诉，这与S在Tk + 1中相矛盾。

# 所以最终算法如下：

# T0是空集。
# 要生成Tk（对于k> 0），请取Tk-1中的每个字符串并尝试追加0和1.这将给出最多202个可能的答案，其中我们保持最佳的101（通常，我们保留顶部M + 1）。
# 采取TP禁止的最佳组合。
# 天真地，这可以在O（P2M）中完成，但也可以在O（PM）中更快地完成。总的来说，算法采用O（PN + P2M）或O（PN + PM）。


def isOdd(n):
    return n % 2


def complain(s1, s2, P):
    tmpc = 0
    for i in range(P):
        if s1[i] != s2[i]:
            tmpc += 1

    return tmpc


def changestr(s, i, c):
    tmps = []
    for tmpi in range(len(s)):
        if tmpi == i:
            tmps.append(c)
        else:
            tmps.append(s[tmpi])
    return "".join(tmps)


def rg(tmps, dis, P):
    org = tmps
    orgd = dis

    for i in range(P):
        tmps = org

        index = dis.index(min(dis))
        dis[index] += 10

        if tmps[index] == "0":
            tmps = changestr(tmps, index, '1')
        else:
            tmps = changestr(tmps, index, '0')
        yield tmps

    tmps = org
    dis = orgd

    index = dis.index(min(dis))
    dis[index] += 10

    if tmps[index] == "0":
        tmps = changestr(tmps, index, '1')
    else:
        tmps = changestr(tmps, index, '0')

    yield from rg(tmps, dis, P)


def source(tmps, A, P):
    total = 0
    for i in range(len(A)):
        total += complain(tmps, A[i], P)
    return total


minans = 9999


def dfs(tmps, A, B, P):
    global minans
    if len(tmps) >= P:
        if tmps not in B:
            minans = min(minans, source(tmps, A, P))
            return 0
        else:
            return 0

    dfs(tmps+"0", A, B, P)
    dfs(tmps+"1", A, B, P)

    return 0


# A 从小到大排列
def solve_EB(N, M, P, A, B):
    ans = 0

    # 计数
    c = [[0 for _ in range(2)] for i in range(P)]

    for a in A:
        for i in range(P):
            if a[i] == '0':
                c[i][0] += 1
            else:
                c[i][1] += 1
    dis = []
    for i in range(P):
        dis.append(abs(c[i][0]-c[i][1]))

    tmps = ""
    for i in range(P):
        if c[i][0] > c[i][1]:
            tmps = tmps + '0'
        else:
            tmps = tmps + '1'

    for s in rg(tmps, dis, P):
        if s not in B:
            total = 0
            for i in range(len(A)):
                total += complain(s, A[i], P)
            break

    return total


def main():
    global minans
    T = int(input())

    for t in range(T):
        tmp = input().split()
        tmp = list(map(int, tmp))
        N, M, P = tmp

        A = []
        for n in range(N):
            A.append(input().split()[0])

        B = []
        for m in range(M):
            B.append(input().split()[0])

        # dfs("", A, B, P)
        print('Case #' + str(t + 1) + ': ', end='')
        print(solve_EB(N, M, P, A, B))


if __name__ == '__main__':
    main()
