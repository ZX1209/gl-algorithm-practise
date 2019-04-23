maxn = 15
a = [0]*maxn
b=  [0]*maxn

tot = 0
key = 0

mp = {}


class res:
    def __init__(self):
        self.v = [0,0,0]
        self.info = 0
        self.typ = 0

    def __lt__(self,tmpres):
        global key
        if self.v[key] != tmpres.v[key]:
            return self.v[key]<tmpres.v[key]
        return self.typ < tmpres.typ

    def print(self):
        print(self.typ,self.v,info)

n = 0
tmp = res()
v = []
tv = []
ttv = []
rescnt = [0,0,0]

maxv = 1600000
sz = [0]*maxv
stamp = [0]*maxv
curt = 0

def lb(x):
    return ((x)&(-(x)))

def add(p):
    global maxv,stamp,sz,curt
    for i in range(p,maxv,lb(i)):
        if stamp[i] != curt:
            sz[i] = 0
            stamp[i] = curt

        sz[i] += 1

def sum(p):
    int res = 0
    for i in range(p,)

def dfs(cur,pos):
    global n,tmp,v
    if pos == 3*n:
        mp[tmp.v[2]] = 0
        v.append(tmp)
        return

    for i in range(3):
        if 

def solve():
    v = []
    mp = {}
    pass





if __name__ == '__main__':
    t= int(input())

    for i in range(1,t+1):
        print("Case #",i,': ',solve())