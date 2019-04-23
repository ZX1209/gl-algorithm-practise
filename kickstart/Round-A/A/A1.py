from logging import *

basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',level=DEBUG)

'''
先看第一位,
如果为偶数则跳到下一位 
如果为奇数 这是就要加一或减一来凑成偶数
这样就要看下一位了,,
要是下一位是偶数,,则要四十五入来加活减到0吧(到0与10的距离)
然后依次递推

总之,先找到革命位(从高到低,最先为奇的数)
之后,递归求解,,求解的数值要根据位数来判断与相加

位数从0开始
'''
#1 represent odd
#o represent even
def isodd(n):
    return n%2

#字符串翻转
def reverse(s):
    return s[::-1]

#传入正的数字字符串
def get_geming(N):
    i = 1
    for w in N:
        if isodd(int(w)):
            return len(N)-i
        i+=1

    return -1

#传入翻转的字符串与奇数位
def  seek_answer(N,i):
    answer1 = 0
    i1=i-1

    answer2 = 0
    i2=i-1

    # +
    # 如果第一位奇数是9的话 用+ 法会产生进位,这样上一位
    #肯定还是奇数,,很麻烦,,也远超减法的值了
    if N[i]=='9':
        answer1=int(N)
    else:
        while i1>=1:
            answer1+=(9-int(N[i1]))*(10**i1)
            i1-=1
        answer1+=10-int(N[0])

    # -
    while i2>=1:
        answer2+=(int(N[i2])+1)*(10**i2)
        i2-=1
    answer2+=int(N[0])+2

    return min(answer1,answer2)







T = int(input())

for i in range(T):
    #debug('this is a debug message')
    N = input()
    answer = 0

    #确定革命位
    gmw=get_geming(N)

    #如果有奇数位的话
    if gmw!=-1:
        if gmw!=0:
            nr = reverse(N)
            answer=seek_answer(nr,gmw)
        else:
            answer=1
            #从这位递归求解


    print('Case #'+str(i+1)+': '+str(answer))
