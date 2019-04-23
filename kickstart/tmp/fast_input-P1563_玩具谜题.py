# #import logging as log
# import sys

# #log.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',level=log.DEBUG)


# def time_record(f):
#     import time
#     def function(*args, **kw):
#         start = time.time()
#         print('====start====')
#         f(*args, **kw)
#         print('====end====')
#         print('total: '+str(time.time()-start))

#     return function


# def tmpfunction(l):
#     for i in l:
#         pass

#     return 0

# def fasttmpfunction(l):
#     for i in range(len(l)):
#         pass
#     return 0

# l  = tuple(tmpi for tmpi in range(10000))
# start = time.time()
# print('====start====')
# for i in l:
#     print(i)
# print('====end====')
# total1 = time.time()-start

# start = time.time()
# print('====start====')
# for i in range(len(l)):
#     print(l[i])
# print('====end====')
# total2 = time.time()-start



# l  = [tmpi for tmpi in range(10000)]
# start = time.time()
# print('====start====')
# for i in l:
#     print(i)
# print('====end====')
# total3 = time.time()-start

# start = time.time()
# print('====start====')
# for i in range(len(l)):
#     print(l[i])
# print('====end====')
# total4 = time.time()-start

# print(total1,total2)
# print(total3,total4)





# class little(object):
#     def __init__(self,name,d):
#         self.name = name
#         self.d = int(d)

#     def __str__(self):
#         return '{name: '+self.name+' ,d:'+str(self.d)+' }'


# def getLittle(l,n):
#     return l[n%len(l)]

# littles = []


# tmp = input().split()
# tmp = tuple(map(int,tmp))
# n,m = tmp


# for tmpi in range(n):
#     tmp = input().split()

# currentLittle = 0
# for tmpi in range(m):
#     tmp = input().split()
#     tmp = tuple(map(int,tmp))
#     d,dis = tmp

# print(getLittle(littles,currentLittle).name)


# #import logging as log
# import sys

# #log.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',level=log.DEBUG)


# class little(object):
#     def __init__(self,name='nono',d):
#         self.name = name
#         self.d = int(d)

#     def __str__(self):
#         return '{name: '+self.name+' ,d:'+str(self.d)+' }'


# def getLittle(l,n):
#     return l[n%len(l)]

# littles = []


# tmp = input().split()
# tmp = tuple(map(int,tmp))
# n,m = tmp


# for tmpi in range(n):
#     tmp = input().split()
#     littles.append(little(tmp[1],tmp[0]))

# currentLittle = 0
# for tmpi in range(m):
#     tmp = input().split()
#     tmp = tuple(map(int,tmp))
#     d,dis = tmp

#     #log.debug('currentLittle: '+str(getLittle(littles,currentLittle))+'next: '+str(d)+' '+str(dis))

#     if getLittle(littles,currentLittle).d!=d:
#         currentLittle+=dis
#     else:
#         currentLittle-=dis

# print(getLittle(littles,currentLittle).name)


import sys
import time


# l = []
# start = time.time()
# for line in sys.stdin:
#     l.append(line)
# total1 = time.time()-start
# print(total1)


start = time.time()
littles = []

tmp = input().split()
tmp = list(map(int,tmp))
n,m = tmp


for tmpi in range(n):
    tmp = input().split()

currentLittle = 0
for tmpi in range(m):
    tmp = input().split()
    tmp = list(map(int,tmp))
    d,dis = tmp
total2 = time.time()-start
print(total2)









