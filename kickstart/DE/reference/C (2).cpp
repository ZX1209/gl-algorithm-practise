#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cmath>
#include <string>
#include <cctype>
#include <vector>
#include <map>
using namespace std;
typedef unsigned long long ULL;
typedef long long LL;
struct document{
	document(){
	#ifndef ONLINE_JUDGE
		freopen("1.in", "r", stdin);
	#endif
	}
} input;
const int maxn = 15;
int a[maxn], b[maxn];

int tot, key;

map<int, int> mp;

//0: ours 1: opponent
struct res{
	int v[3], info;
	bool typ;

	bool operator < (const res &an) {
		if (v[key] != an.v[key])
			return v[key] < an.v[key];
		return typ < an.typ;
	}

	void print() const {
		printf("(%d) %d %d %d: %d\n", typ, v[0], v[1], v[2], info);
	}
};
int n;
res tmp;
vector<res> v;
vector<res> tv;
vector<int> ttv;
int rescnt[3];

const int maxv = 1600000;
int sz[maxv], stamp[maxv], curt;
#define lb(x) ((x)&(-(x)))
void add(int p) {
	for (int i=p; i<maxv; i+=lb(i)) {
		if (stamp[i] != curt) {
			sz[i] = 0;
			stamp[i] = curt;
		}
		sz[i] ++;
	}
}
int sum(int p) {
	int res = 0;
	for (int i=p; i; i-=lb(i)) {
		if (stamp[i] == curt)
			res += sz[i];
	}
	return res;
}

void dfs(int *cur, int pos) {
	if (pos == 3*n) {
		mp[tmp.v[2]] = 0;
		v.push_back(tmp);
		return;
	}
	for (int i=0; i<3; i++) {
		if (rescnt[i] == n)
			continue;
		tmp.v[i] += cur[pos];
		rescnt[i]++;
		dfs(cur, pos+1);
		tmp.v[i] -= cur[pos];
		rescnt[i]--;
	}
}

void printv() {
	puts("======");
	for (auto &p: v) {
	 	p.print();
	}
	puts("======");
}

void get(int l, int r) {
	if (l == r)
		return;
	int mid = (l+r)>>1;
	get(l, mid);
	get(mid+1, r);

	curt++;
//	printf("solve %d-%d\n", l, r);
	int lp = l, rp = mid+1, p = l, cnt = 0;
	while (p <= r) {
		if (lp > mid || (rp <= r && v[lp].v[1] >= v[rp].v[1])) {
			if (!v[rp].typ) {
				v[rp].info -= 2*sum(v[rp].v[2]-1);
				v[rp].info += cnt;
			}
			ttv[p++] = rp++;
		} else {
			if (v[lp].typ) {
				add(v[lp].v[2]);
				cnt++;
			}
			ttv[p++] = lp++;
		}
	}
	for (int i=mid+1; i<=r; i++) {
		if (!v[i].typ) {
			v[i].info += sum(v[i].v[2]-1);
		}
	}
	for (int i=l; i<=r; i++)
		tv[i] = v[ttv[i]];
	for (int i=l; i<=r; i++)
		v[i] = tv[i];
//	printv();
}

void get2(int l, int r) {
	if (l == r)
		return;
	int mid = (l+r)>>1;
	get2(l, mid);
	get2(mid+1, r);

	int lp = l, rp = mid+1, p = l, cnt = 0;
	while (p <= r) {
		if (lp > mid || (rp <= r && v[lp].v[1] >= v[rp].v[1])) {
			if (!v[rp].typ) {
				v[rp].info += cnt;
			}
			tv[p++] = v[rp++];
		} else {
			if (v[lp].typ) {
				cnt++;
			}
			tv[p++] = v[lp++];
		}
	}
	for (int i=l; i<=r; i++)
		v[i] = tv[i];
}

double solve() {
	v.clear();
	mp.clear();
	cin >> n;
	for (int i=0; i<3*n; i++) {
		cin >> a[i];
	}
	for (int i=0; i<3*n; i++) {
		cin >> b[i];
	}
	tmp.typ = 0;
	dfs(a, 0);
	tmp.typ = 1;
	dfs(b, 0);
	int cur = 0;
	for (auto &p: mp) {
		p.second = ++cur;
	}
	for (auto &p: v) {
		p.v[2] = mp[p.v[2]];
	}

	key = 0;
	tv.resize(v.size());
	ttv.resize(v.size());
	sort(v.begin(), v.end());
	get(0, v.size()-1);
//	printv();

	key = 2;
	sort(v.begin(), v.end());
	get2(0, v.size()-1);

//	printv();
	int ans = 0;
	for (auto &p: v) {
		if (!p.typ) {
			ans = max(ans, p.info);
		}
	}
	return ans * 2.0 / v.size();
}

int main(){
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		fprintf(stderr, "Case #%d\n", tt);
		printf("Case #%d: %.9f\n", tt, solve());
	}
	return 0;
}
