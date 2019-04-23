def main():
    Maxn = 1001

    n = 0
    m = 0
    Set = [0]*Maxn
    data = [[0]*Maxn for i in range(Maxn)]
    Chord = 0

    def Relabel():
        num,j,Max,MaxValue = 0,0,0,0
        Link = [0]*Maxn
        Used = [0]*Maxn
        Used[1] = 1


        for num in range(n-1,0,-1):
            Link = [0]*Maxn
            for i in range(1,n+1):
                if not Used[i]:
                    for j in range(1,n-num+1):
                        if Data[i][Set[n-j+1]]:
                            Link[i]+=1

            MaxValue = 0
            for i in range(1,n+1):
                if Link[i]>MaxValue:
                    MaxValue = Link[i]
                    Max = i 

            Set[num] = Max
            Used[Max] = 1

    def Check():
        i,j,t = 0,0,0
        Temp = [0]*Maxn 
        i = 1
        while i<=n and Chord:
            Temp = [0]*Maxn 
            t = 0
            for j in range(i+1,n+1):
                if Data[Set[i]][Set[j]]:
                    t+=1
                    Temp[t] = Set[j]

            for j in range(2,t+1):
                if not Data[Temp[j]][Temp[1]]:
                    Chord = 0
                    break

            i+=1 
    while True:
        tmp = input().split()
        tmp = list(map(int,tmp))
        if tmp==(0,0):
            break

        n,m = tmp
        data = [[0]*Maxn for i in range(Maxn)]
        p,q = 0,0
        for i in range(1,m+1):
            tmp = input().split()
            p,q = list(map(int,tmp))
            Data[p][q] = 1
            Data[q][p] = 1

        Set[n] = 1
        Relabel()
        Chord = 1
        Check()
        if Chord: print("Perfect")
        else: print("Perfect")
    return 0






if __name__ == '__main__':
    main()