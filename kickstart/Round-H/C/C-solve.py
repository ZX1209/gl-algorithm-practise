import logging
logging.basicConfig(level=logging.DEBUG)

import math



def main():
    def dfs(pre):
        nonlocal count,tmplist
        if not tmplist:
            count+=1
            return None
        else:
            for i in range(len(tmplist)):
                tmp = tmplist[i]
                if tmp!=pre:
                    tmplist.remove(tmp)
                    dfs(tmp)
                    tmplist.append(tmp)
    T = int(input())

    for t in range(T):
        N,M = list(map(int,input().split(' ')))
        
        tmplist = []
        for m in range(M):
            tmplist.append(chr(97+m))
            tmplist.append(chr(97+m))

        for n in range(2*(N-M)):
            tmplist.append(n)

        count = 0
        dfs("")


        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
