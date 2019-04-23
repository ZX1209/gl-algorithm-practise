import logging as log
import multiprocessing as mp
threads = []

log.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m', slevel=log.INFO)


def isodd(n):
    return n % 2


def reverse_sign(n):
    return -n


def if_test(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
# 最大子串和
# O 是子串中奇数的最大个数
# D 是子串和的最大值,如非正,转换num_list 与 D


def maximum_section_DA(num_list, O, D):
    totalodd = 0
    tmpsum = 0
    maxsum = sum([tmpi for tmpi in num_list if tmpi < 0])

    for tmpi in range(len(num_list)):
        tmpsum += num_list[tmpi]
        if(isodd(num_list[tmpi])):
            totalodd += 1

        if tmpsum < 0:
            tmpsum = 0
            totalodd = 0
        elif totalodd > O or tmpsum > D:
            tmpsum = 0
            totalodd = 0
        elif(tmpsum > maxsum):
            maxsum = tmpsum

    return maxsum


def DA_solve(num_list, O, D):
    def so(l, r):
        if l > r:
            return 0
        tmpodd = 0
        for tmpi in range(l, r+1):
            if(isodd(num_list[tmpi])):
                tmpodd += 1
        return tmpodd

    def ss(l, r):
        if l > r:
            return 0
        tmpsum = 0
        for tmpi in range(l, r+1):
            tmpsum += num_list[tmpi]

        return tmpsum

    start = 0
    maxsum = num_list[0]
    ischanged = 0
    ispostive = 1
    if D < 0:
        D = -D
        num_list = list(map(reverse_sign, num_list))
        ispostive = 0

    for end in range(len(num_list)):
        tmpoddsum = so(start, end)
        tmptmpsum = ss(start, end)

        while tmpoddsum > O:
            start += 1
            tmpoddsum = so(start, end)

        while tmptmpsum > D:
            start += 1
            tmptmpsum = ss(start, end)

        if tmptmpsum < 0 and start < end:
            start = end+1
            tmptmpsum = ss(start, end)

        elif tmptmpsum > maxsum:
            ischanged = 1
            maxsum = tmptmpsu

        if ispostive:
            print(maxsum)
        else:
            print(-maxsum)
    else:
        print('IMPOSSIBLE')

    return 0


    # if ischanged:
    #     if ispostive:
    #         print(mp.current_process().name+str(maxsum))
    #     else:
    #         print(mp.current_process().name+str(-maxsum))
    # else:
    #     print(mp.current_process().name+'IMPOSSIBLE')

    # return 0


# def maxSum_test(list_of_nums):
#     global D,O
#     if D>0:
#         maxsum = 0
#         maxtmp = 0
#         for i in range(len(list_of_nums)):
#             if maxtmp <= 0:
#                 maxtmp = list_of_nums[i]
#             else:
#                 maxtmp += list_of_nums[i]

#             if(maxtmp > maxsum):
#                 maxsum = maxtmp

#     else:
#         maxsum = 0
#         maxtmp = 0
#         for i in range(len(list_of_nums)):
#             if maxtmp > 0:
#                 maxtmp = list_of_nums[i]
#             else:
#                 maxtmp += list_of_nums[i]

#             if(maxtmp > maxsum):
#                 maxsum = maxtmp


# def maxSum(list_of_nums):
#     global D,O
#     maxsum = 0
#     maxtmp = 0
#     totalodd = 0


#     for i in range(len(list_of_nums)):
#         # try
#         maxtmp += list_of_nums[i]

#         if(isodd(list_of_nums[i])):
#             totalodd+=1

#         if maxtmp>D or totalodd>O or maxtmp<0:
#             totalodd = 0
#             maxtmp = 0


#         if maxtmp>maxsum:
#             maxsum=maxtmp

#     return maxsum

# def findmin(numberList):
#     global D,O
#     minsum = 0
#     mintmp = 0
#     totalodd = 0

#     for i in range(len(numberofList)):
#         # try
#         maxtmp += list_of_nums[i]

#         if(isodd(list_of_nums[i])):
#             totalodd+=1

#         if mintmp>D or totalodd>O:
#             totalodd = 0
#             maxtmp = list_of_nums[i]
#             if(isodd(list_of_nums[i])):
#                 totalodd+=1


#         if mintmp<minsum:
#             minsum = mintmp


# def DA_DFS(total):
#     global max,nstatus,nodds
#     if(total>D):
#         return 0
#     elif total==D:
#         max = D
#         return 0
#     else:
#         if total>max:
#             max = total


#     for tmpi in range(len(nodds)):
#         if nstatus[tmpi]==0:
#             nstatus[tmpi]=1
#             DA_DFS(total+nodds[tmpi])
#             nstatus[tmpi]=0

#     return 0


T = int(input())

for n in range(T):
    log.debug('this is a debug message')
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

    
    print('Case #'+str(n+1)+': ',end='')
    DA_solve(tuple(S), O, D)