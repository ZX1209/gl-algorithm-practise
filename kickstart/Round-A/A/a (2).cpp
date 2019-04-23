#include <bits/stdc++.h>
using namespace std;
#define db(x) cerr << #x << "=" << x << endl
#define db2(x, y) cerr << #x << "=" << x << "," << #y << "=" << y << endl
#define db3(x, y, z) cerr << #x << "=" << x << "," << #y << "=" << y << "," << #z << "=" << z << endl
typedef long long ll;
typedef long double ld;
char n[25];
ll eights[25], p10[25];
int main() {
	p10[0] = 1;
	for (int i = 1; i <= 18; ++i) {
		eights[i] = eights[i - 1] * 10 + 8;
		p10[i] = p10[i - 1] * 10;
	}
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		ll v;
		scanf("%lld", &v);
		ll w = 0;
		for (int i = 17; i >= 0; --i) {
			for (int d = 0; d <= 8; d += 2) {
				if ((w * 10 + d) * p10[i] + eights[i] >= v) {
					w = w * 10 + d;
					break;
				}
			}
		}
		assert(w >= v);
		ll ans = w - v;
		w = 0;
		for (int i = 17; i >= 0; --i) {
			for (int d = 8; d >= 0; d -= 2) {
				if ((w * 10 + d) * p10[i] <= v) {
					w = w * 10 + d;
					break;
				}
			}
		}
		assert(w <= v);
		ans = min(ans, v - w);
		printf("Case #%d: %lld\n", cn, ans);
	}
}

