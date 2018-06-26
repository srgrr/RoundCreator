----------
RoundCreator
----------
A very simple, small tool I developed some years ago. It creates a folder structure for programming contest problems. It works for Python 2.7 and Python 3.
Due to the argparse dependency, it won't work on Python 2.6. It works and creates appropriate scripts for Windows and Linux.

----------
Installation
----------
If you have downloaded the tar.gz, you can type python setup.py install. This will install a package named "RoundCreator". Read the following sections for further explanation.

----------
General overview
----------

RoundCreator is a very typical script which accepts some arguments and then does some stuff. Its arguments (and its default values) are:
* --name Contest name. Its default value is "myContest"
* --amount Number of problems. Its default value is 5
* --until Letter of the last problem. Its default value is 'e' (which is equal to 5)
* --single Type it if you want a single problem. It will place the source and scripts in the contest folder. Its default value is False
* --author Your name. If not specified, it won't appear in your source code template.
* --hightail Type this if you want to have a hightail configuration file in your contest folder
----------
A simple example
----------
Let's suppose you are competing in a contest named "hardContest" which has two problems (a and b), then, the following command:
RoundCreator --name hardContest --amount 2


Will create the following folder structure:

hardContest
├── a
│   ├── compile.sh
│   ├── input.txt
│   ├── main.cpp
│   ├── output.txt
│   └── test.sh
└── b
    ├── compile.sh
    ├── input.txt
    ├── main.cpp
    ├── output.txt
    └── test.sh

----------
Templates
----------
The code templates are the following. At the moment there is no way to change them.
Any suggestion on how to implement this feature in an elegant way is welcome.

----------
C++ source code
----------
/*
    Author: YourName (if specified)
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
}

----------
Compile script
----------

g++ main.cc -Wall -Wextra -pedantic -std=c++11 -O2 -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -D_FORTIFY_SOURCE=2 -fsanitize=address -fstack-protector

----------
Test script
----------
Windows:
a.exe < input.txt
Linux:
./a.out < input.txt
