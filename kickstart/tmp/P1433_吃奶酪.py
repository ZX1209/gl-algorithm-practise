# P1433 吃奶酪
cheses = [(0,0)]
ispassed = []
disto = []
result = 1000
n = 0

def dfs(pre,dis):
    global result,ispassed,cheses,disto,n
    if dis<result:
        if 0 in ispassed:
            for i in range(n+1):
                if ispassed[i]==0:
                    ispassed[i]=1
                    dfs(i,dis+disto[pre][i])
                    ispassed[i]=0
        else:
            if result>dis:
                result = dis
    else:
        return 0

if __name__ == '__main__':
    tmp = input().split()
    tmp = int(tmp[0])
    n = tmp

    for i in range(n):
        tmp = input().split()
        tmp = tuple(map(int,tmp))
        cheses.append(tmp)

    ispassed = [0]*len(cheses)
    ispassed[0]=1


    disto = [[0 for i in range(n+1)] for j in range(n+1)]
    # 距离数组
    for i in range(n+1):
        for j in range(n+1):
            x1=cheses[i][0]
            y1=cheses[i][1]
            x2=cheses[j][0]
            y2=cheses[j][1]
            # print(i,j,disto[i])
            disto[i][j]=((x1-x2)**2+(y1-y2)**2)**(1/2)      
            

    dfs(0,0)
    print('{:.2f}'.format(result))


for i in range(10):
    for j in range(10):
        for k in range(10):
            if i+j+k>10:
                break
            else:
                print(i,j,k)