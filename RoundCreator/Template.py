class Template(object):

	def __init__(self, pattern):
		self.pattern = pattern

	def apply(self, subst_rules = {}):
		ret = self.pattern
		for (k, v) in subst_rules.items():
			ret = ret.replace(k, v)
		return ret

_CPP_SOURCE = """/*
    Template by RoundCreator
    https://github.com/srgrr/RoundCreator
    
    Author: ##AUTHOR##
*/
#include <bits/stdc++.h>
using namespace std;
using ll = long long int;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;

int main() {
  ios_base::sync_with_stdio(0); cin.tie(0);
  
}
"""

CPP_TEMPLATE     = Template(_CPP_SOURCE)

_COMPILE_SOURCE = """g++ main.cc -Wall -Wextra -pedantic -std=c++14 -O2 -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -D_FORTIFY_SOURCE=2 -fsanitize=address -fstack-protector
"""

COMPILE_TEMPLATE = Template(_COMPILE_SOURCE)