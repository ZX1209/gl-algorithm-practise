# A. Common Anagrams

def limit(i,j,k=1):
    yield from range(i,j+1,k)

from collections import defaultdict
def hasSub(A,B):
    l = len(A)
    dic = defaultdict(int)

    i = 0
    while i<l:
        dic[A[i]]-=1
        dic[B[i]]+=1
        i+=1

    lb = len(B)
    while i<lb:
        if any(dic.values()):
            dic[B[i-l]]-=1
            dic[B[i]]+=1
            i+=1
        else:
            return True

    if any(dic.values()):
        return False
    else:
        return True


def main():
    T = int(input())

    for t in range(T):
        L = int(input())

        tmp = input()
        A = tmp

        tmp = input()
        B = tmp

        count = 0

        setb = set(B)
        for a in A:
            if a in setb:
                count+=1

        # if sorted(A) == sorted(B):
        #     count += 1

        i=0
        while i<L:
            for j in limit(i+2,L):
                if hasSub(A[i:j],B):
                    # print(A[i:i+dis],B)
                    count+=1
                else:
                    break
            i+=1

        print("Case #"+str(t+1)+": "+str(count))


if __name__ == '__main__':
    main()
