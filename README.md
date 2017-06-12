# RoundCreator
A very simple, small tool I developed some years ago. It creates a folder structure for programming contest problems. It works for Python 2.7 and Python 3.
Due to the argparse dependency, it won't work on Python 2.6. It works and creates appropriate scripts for Windows and Linux.

## Installation
If you have cloned this repo, you can type `python setup.py install`. This will install a package called "RoundCreator".
## General overview
RoundCreator is a very typical script that accepts some arguments and then does some stuff. Its arguments (and its default values) are:
* `--name` Contest name. Its default value is "myContest"
* `--amount` Number of problems. Its default value is 5
* `--until` Letter of the last problem. Its default value is 'e' (which is equal to 5).
* `--single` Type it plus a random char if you want a single problem. It will place the source and scripts in the contest folder. Its default value is False
* `--author` Your name. If not specified, it won't appear in your source code template.
* `--hightail` Type it plus a random char if you want a hightail.config file appear on your contest root directory.

## A simple example
Let's suppose you are competing in a contest called "hardContest" which has two problems (a and b), then, the following command:<br>
`RoundCreator --name hardContest --amount 2`


Will create the following folder structure:

hardContest<br>
├── a<br>
│   ├── compile.sh<br>
│   ├── input.txt<br>
│   ├── main.cpp<br>
│   ├── output.txt<br>
│   └── test.sh<br>
└── b<br>
    ├── compile.sh<br>
    ├── input.txt<br>
    ├── main.cpp<br>
    ├── output.txt<br>
    └── test.sh<br>
<br>

## Templates
The code templates are the following:
### C++ source code
```c++
/*
    Author: YourName (if specified)
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
}
```
### Compile script
`g++ main.cpp -Wall -O2 -DLOCAL -std=c++11`

### Test script
Windows:<br>
`a.exe < input.txt`<br>
Linux:<br>
`./a.out < input.txt`
