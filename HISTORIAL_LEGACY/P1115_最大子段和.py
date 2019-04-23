N = int(input())

A = input().split()
A = list(map(int,A))

tmpsum = 0
maxsum = sum([tmpi for tmpi in A if tmpi<0])

for tmpi in range(len(A)):
    tmpsum+=A[tmpi]

    if(tmpsum>maxsum):
        maxsum = tmpsum

    if tmpsum<0:
        tmpsum=0

    

print(maxsum)


def 正负号互换(num):
    return -num

def 最大子段和(num_list):
    tmpsum = 0
    maxsum = sum([tmpi for tmpi in num_list if tmpi<0])

    for tmpi in range(len(num_list)):
        tmpsum+=A[tmpi]

        if(tmpsum>maxsum):
            maxsum = tmpsum

        if tmpsum<0:
            tmpsum=0

    return maxsum
