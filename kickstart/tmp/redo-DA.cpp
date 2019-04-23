#include<stdio.h>
#include<vector>

const int MAXN = 500005;

int X[MAXN];
int S[MAXN];
long long sum[MAXN];

int isOdd(int n){
    return n % 2;
}

int os(vector & num_list,int l,int r){
        if (l > r){
            return 0;
        }
        int totalodd = 0;
        for(int i=l;i<r+1;i++){
            if (isOdd(num_list[i])){
                totalodd += 1;
            }
        }
        return totalodd    
}

int ss(vector &sums,int l,int r){
        if (l > r){
            return 0;
        }
        totals = sums[l]-sums[r-1]
        return totals

}
    
int DA_solve(vector &num_list,int O,int D){
    int L = 0;
    int R = 0;
    int length = num_list.length;
    long long maxsum = -0x3f3f3f3f3f3f3f3fLL;

    
    while (R < length){
        while (os(L, R) > O && L < R){
            L += 1;
        }

        while (ss(L, R) > D && L < R){
            L += 1;
        }

        tmpsum = ss(L, R);
        if (tmpsum > maxsum){
            maxsum = tmpsum;
        }

        R += 1;

    }
        
    if (maxsum == -99999 || maxsum > D){

        printf("IMPOSSIBLE\n");
    }
    else:
        printf("%d\n",maxsum);

    return 0;


}
    
int main(){
    int T = 0;
    int N,O,D;
    int x1, x2, A, B, C, M, L;
    scanf('%d',&T);

    for (int i = 0; i < T; ++i)
    {   
        scanf("%d %d %d",&N,&O,&P);
        scnaf("%d %d %d %d %d %d %d",&x1, &x2, &A, &B, &C, &M, &L);
        X[0]=x1;X[1]=x2;
        for (int i = 3; i <= N; i++) {
        X[i] = (1LL * A * X[i - 1] + 1LL * B * X[i - 2] + C) % M;
        }
        for (int i = 1; i <= N; i++) {
            S[i] = X[i] + L;
            sum[i] = sum[i - 1] + S[i];
        }
    }

    for n in range(T):
        tmp = input().split()
        tmp = list(map(int, tmp))
        N, O, D = tmp

        tmp = input().split()
        tmp = list(map(int, tmp))
        x1, x2, A, B, C, M, L = tmp

        X = [x1, x2]
        S = [x1 + L, x2 + L]

        for i in range(2, N):
            X.append((A * X[i - 1] + B * X[i - 2] + C) % M)
            S.append(X[i] + L)

        print('Case #' + str(n + 1) + ': ', end='')
        DA_solve(tuple(S), O, D)

}
    