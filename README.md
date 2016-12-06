# RoundCreator
A very simple, small tool I developed some years ago. It creates a folder structure for programming contest problems.
## A simple example
Let's suppose you are competing in a contest called "hardContest" which has two problems (a and b), then, the following command:<br>
`python RoundCreator.py --name hardContest --amount 2`


Will create the following folder structure:

├───hardContest<br>
│   ├───a<br>
│   │       compile.bat<br>
│   │       input.txt<br>
│   │       main.cpp<br>
│   │       output.txt<br>
│   │       test.bat<br>
│   │<br>
│   └───b<br>
│   │       compile.bat<br>
│   │       input.txt<br>
│   │       main.cpp<br>
│   │       output.txt<br>
│   │       test.bat<br>
│<br>

## Template
By default, the scripts templates are the following:
### C++ source code
```c++
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

}
```
### Compile script
`g++ main.cpp -Wall -O2 -DLOCAL -std=c++11`

### Test script
Windows:<br>
`a.exe < input.txt`<br>
Linux:<br>
`./a.out < input.txt`
