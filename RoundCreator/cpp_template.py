source = '''#include <bits/stdc++.h>
using namespace std;
using ll = long long int;

int next_int() {
  int x;
  if(scanf("%d", &x) != 1) exit(1);
  return x;
}

ll next_ll() {
  ll x;
  if(scanf("%lld", &x) != 1) exit(1);
  return x;
}

double next_double() {
  double x;
  if(scanf("%lf", &x) != 1) exit(1);
  return x;
}

string next_string() {
  static char buf[1000000];
  if(scanf("%s", buf) != 1) exit(1);
  return string(buf);
}

char next_char() {
  char x;
  if(scanf("%c", &x) != 1) exit(1);
  return x;
}

int main() {
  ios_base::sync_with_stdio(0); cin.tie(0);
}
'''
