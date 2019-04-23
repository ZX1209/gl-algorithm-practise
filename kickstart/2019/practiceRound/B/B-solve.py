def dfs(D,l,r,tmpS,N,maxS):
    if N==0:
        if maxS[0] > tmpS:
            maxS[0] = tmpS
    else:
        dfs(D,l+1,r,tmpS+D[l],N-1,maxS)
        dfs(D,l,r-1,tmpS+D[r],N-1,maxS)

def main():
    T = int(input())

    for t in range(T):
        N = int(input())
        D = [int(c) for c in input()]
        total  = sum(D)
        maxS = [total]

        dfs(D,0,N-1,0,N//2,maxS)


        print("Case #"+str(t+1)+": "+str(total-maxS[0]))



if __name__ == '__main__':
    main()




        # waterWalls = [0,len(D)]
        

        # count = 0

        # tmpmax = max(D)
        # tmpindex = D.index(tmpmax)
        # count+=tmpmax

        # D[tmpindex] = -1 # for painted


        # paintWalls = []
        # if 0<=tmpindex-1<len(D):
        #     paintWalls.append(tmpindex-1)
        # elif 0<=tmpindex+1<len(D):
        #     paintWalls.append(tmpindex+1)

        # if D[waterWalls[0]]>D[waterWalls[1]]:
        #     D[waterWalls[0]] = -1
        #     waterWalls[0] += 1
        # elif D[waterWalls[0]]<D[waterWalls[1]]:
        #     D[waterWalls[1]] = -1
        #     waterWalls[1] -=1
        # else:
        #     if D[waterWalls[1]] == -1:
        #         break

        #     # todo bigger
        #     D[waterWalls[0]] = -1
        #     waterWalls[0] += 1



