import logging as log

log.basicConfig(level=log.INFO)



T = int(input())

for t in range(T):
    log.debug('this is a debug message')
    ans = 0
    N = input()
    N = [c for c in N]

    firstOddIndex = -1
    for i,c in enumerate(N):
        if (ord(c)-ord('0'))%2:
            firstOddIndex = i
            break

    if firstOddIndex==-1:
        ans = 0
    else:
        tmpplus = N.copy()
        tmpmins = N.copy()

        # who cares the first 0
        tmp = tmpmins[firstOddIndex]
        tmpmins[firstOddIndex] = chr(int(tmp)-1+ord('0'))

        for i in range(firstOddIndex+1,len(N)):
            tmpmins[i] = '8'

        if N[firstOddIndex]=='9':
            tmpplus = ["0"]+tmpplus
            firstOddIndex+=1

            while tmpplus[firstOddIndex-1]=='8':
                firstOddIndex-=1

            firstOddIndex-=1

            tmp= tmpplus[firstOddIndex]
            tmpplus[firstOddIndex] = chr(int(tmp)+1+ord('0'))

        tmp= tmpplus[firstOddIndex]
        tmpplus[firstOddIndex] = chr(int(tmp)+1+ord('0'))
        for i in range(firstOddIndex+1,len(N)):
            tmpplus[i] = '0'


        tmpplus  = "".join(tmpplus)
        tmpmins = "".join(tmpmins)
        N = "".join(N)
        ans = min(int(tmpplus)-int(N),int(N)-int(tmpmins))

        



    print('Case #'+str(t+1)+': '+str(ans))
