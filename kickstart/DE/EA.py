# EA.py

def isOdd(n):
    return n % 2

# A 从小到大排列
def solve_EA(N,K,A):
    ans = 0

    n = 0
    while n<N:
        k = 0
        while k<K:
            if len(A)>0:
                if A[0]>n:
                    A.pop(0)
                    k+=1
                    ans+=1  
                else:
                    A.pop(0)
            else:
                return ans
        n+=1

    return ans



def main():
    T = int(input())

    for t in range(T):
        tmp = input().split()
        tmp = list(map(int, tmp))
        N, K = tmp

        tmp = input().split()
        tmp = list(map(int, tmp))
        A = tmp

        A.sort()

        print('Case #' + str(t + 1) + ': ', end='')
        print(solve_EA(N,K,A))


if __name__ == '__main__':
    main()
