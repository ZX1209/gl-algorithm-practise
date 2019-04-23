#include<bits/stdc++.h>
using namespace std;
int T,n,m,p,i,j,k,w[105][2],c[10005][2],N,ans;
char a[105][105],b[105][105];
struct node
{
	int s;
	bool c[105];
	bool operator<(const node& y)const
	{
		return s>y.s;
	}
}t;
priority_queue<node> h;
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	for(int xxx=1;xxx<=T;xxx++)
	{
		printf("Case #%d: ",xxx);
		scanf("%d%d%d",&n,&m,&p);
		for(i=0;i<n;i++)scanf("%s",a[i]);
		for(i=0;i<m;i++)scanf("%s",b[i]);
		memset(c,0,sizeof(c));
		memset(w,0,sizeof(w));
		while(!h.empty())h.pop();
		for(i=0;i<p;i++)
		{
			for(j=0;j<n;j++)w[i][a[j][i]^'1']++;
			if(w[i][0]>w[i][1])for(swap(w[i][0],w[i][1]),j=0;j<m;j++)b[j][i]^=1;
		}
		for(N=1,i=0;i<m;i++)for(j=1,k=0;k<p;j=c[j][b[i][k++]^'0'])if(!c[j][b[i][k]^'0'])c[j][b[i][k]^'0']=++N;
		memset(t.c,0,sizeof(t.c));
		for(i=t.s=0;i<p;i++)t.s+=w[i][0];
		h.push(t);
		for(;;)
		{
			t=h.top();
			h.pop();
			for(i=0,j=1;i<p;j=c[j][t.c[i++]]);
			if(!j)break;
			for(i=0;i<p;i++)if(!t.c[i])
			{
				t.c[i]=1;
				t.s+=w[i][1]-w[i][0];
				h.push(t);
				t.c[i]=0;
				t.s-=w[i][1]-w[i][0];
			}
		}
		printf("%d\n",t.s);
	}
	return 0;
}

