#include <bits/stdc++.h>

using namespace std;

void dfs(vector<int>& a, int p, vector<int> v1, vector<int> v2, vector<int> v3, vector<tuple<int, int, int>>& ans) {
  if (v1.size() * 3 > a.size() || v2.size() * 3 > a.size() || v3.size() * 3 > a.size()) {
    return;
  }
  if (p == a.size()) {
    int x = accumulate(v1.begin(), v1.end(), 0);
    int y = accumulate(v2.begin(), v2.end(), 0);
    int z = accumulate(v3.begin(), v3.end(), 0);
    ans.push_back({x, y, z});
    return;
  }
  v1.push_back(a[p]);
  dfs(a, p + 1, v1, v2, v3, ans);
  v1.pop_back();
  v2.push_back(a[p]);
  dfs(a, p + 1, v1, v2, v3, ans);
  v2.pop_back();
  v3.push_back(a[p]);
  dfs(a, p + 1, v1, v2, v3, ans);
  v3.pop_back();
}

template <class T> struct FenwickTree {
  int N;
  std::vector<T> in;
  FenwickTree(int N) : N(N), in(N) {}
  void add(int at, T by) {
    for (int i = at; i < N; i += (i & -i)) {
      in[i] += by;
    }
  }
  T query(int at) {
    T sum = 0;
    for (int i = at; i; i -= (i & -i)) {
      sum += in[i];
    }
    return sum;
  }
};

vector<int> two_count(vector<pair<int, int>> v1, vector<pair<int, int>> v2) {
  FenwickTree<long long> ft(5555555);
  vector<tuple<int, int, int>> vec;
  for (int i = 0; i < v1.size(); i++) {
    vec.emplace_back(v1[i].first, -i, v1[i].second);
  }
  for (auto [x, y] : v2) {
    vec.emplace_back(x, 1, y);
  }
  sort(vec.begin(), vec.end());
  vector<int> ans(v1.size());
  for (auto [x, id, y] : vec) {
    if (id == 1) {
      ft.add(y, 1);
    } else {
      ans[-id] = ft.query(y - 1);
    }
  }
  return ans;
}

FenwickTree<long long> ft(5555555);

typedef tuple<int, int, int, int> Query;

vector<Query> cdq(vector<Query> vec, vector<int>& ans) {
  if (vec.size() <= 1)
    return vec;
  int m = vec.size() / 2;
  auto left = cdq({vec.begin(), vec.begin() + m}, ans);
  auto right = cdq({vec.begin() + m, vec.end()}, ans);
  vector<Query> ret;
  int h1 = 0, h2 = 0;
  while (h1 < left.size() || h2 < right.size()) {
    if (h2 == right.size() || (h1 < left.size() && get<2>(left[h1]) < get<2>(right[h2]))) {
      if (get<1>(left[h1]) == 1){
        ft.add(get<3>(left[h1]), 1);
      }
      ret.push_back(left[h1++]);
    } else {
      if (get<1>(right[h2]) != 1){
        ans[-get<1>(right[h2])] += ft.query(get<3>(right[h2]) - 1);
      }
      ret.push_back(right[h2++]);
    }
  }
  for (auto q : left) {
    if (get<1>(q) == 1){
      ft.add(get<3>(q), -1);
    }
  }
  return ret;
}

vector<int> three_count(vector<tuple<int, int, int>> v1, vector<tuple<int, int, int>> v2) {
  vector<Query> vec;
  for (int i = 0; i < v1.size(); i++) {
    int x, y, z;
    tie(x, y, z) = v1[i];
    vec.emplace_back(x, -i, y, z);
  }
  for (auto [x, y, z] : v2) {
    vec.emplace_back(x, 1, y, z);
  }
  sort(vec.begin(), vec.end());
  vector<int> ans(v1.size());
  cdq(vec, ans);
  return ans;
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;
  
  for (int cas = 0; cas < T; cas++) {
    int n;
    cin >> n;
    vector<int> a(n * 3, 0), b(n * 3);
    for (int i = 0; i < n * 3; i++) {
      cin >> a[i];
    }
    for (int i = 0; i < n * 3; i++) {
      cin >> b[i];
    }
    vector<tuple<int, int, int>> v1, v2;
    dfs(a, 0, vector<int>(), vector<int>(), vector<int>(), v1);
    dfs(b, 0, vector<int>(), vector<int>(), vector<int>(), v2);
    vector<int> ans(v1.size());
    for (int i = 0; i < 1 << 3; i++) {
      if (__builtin_popcount(i) == 2) {
        vector<int> ids;
        for (int j = 0; j < 3; j++) {
          if ((1 << j) & i) {
            ids.push_back(j);
          }
        }
        vector<pair<int, int>> vec1, vec2;
        for (auto e : v1) {
          vector<int> vv = {get<0>(e), get<1>(e), get<2>(e)};
          vec1.emplace_back(vv[ids[0]], vv[ids[1]]);
        }
        for (auto e : v2) {
          vector<int> vv = {get<0>(e), get<1>(e), get<2>(e)};
          vec2.emplace_back(vv[ids[0]], vv[ids[1]]);
        }
        auto ret = two_count(vec1, vec2);
        for (int i = 0; i < ret.size(); i++) {
          ans[i] += ret[i];
        }
      }
    }
    auto ret = three_count(v1, v2);
    for (int i = 0; i < ret.size(); i++) {
      ans[i] -= 2 * ret[i];
    }
    int mx = 0;
    for (auto x : ans) {
      mx = max(x, mx);
    }
    printf("Case #%d: %.10f\n", cas + 1, 1.0 * mx / v2.size());
  }
  return 0;
}

