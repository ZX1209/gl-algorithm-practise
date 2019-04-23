#import logging as log
#log.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',level=log.DEBUG)


class little(object):
    def __init__(self,name,d):
        self.name = name
        self.d = d


littles = []


tmp = input().split()
tmp = tuple(map(int,tmp))
n,m = tmp

for tmpi in range(n):
    tmp = input().split()
    littles.append(little(tmp[1],tmp[0]))

currentLittle = 0
for tmpi in range(m):
    tmp = input().split()
    d = tmp[0]
    dis = int(tmp[1])

    #log.debug('currentLittle: '+str(getLittle(littles,currentLittle))+'next: '+str(d)+' '+str(dis))

    if littles[currentLittle%n].d!=d:
        currentLittle+=dis
    else:
        currentLittle-=dis

print(littles[currentLittle%n].name)




