-----------------
|  **`Travis CI Status`**   |
|-------------------|
|[![Travis](https://img.shields.io/travis/srgrr/RoundCreator.svg)](https://travis-ci.org/srgrr/RoundCreator)|

# RoundCreator
Create a folder structure for programming contest problems. It is intended to work in Python 3 and in Linux environments, but that does not mean that it cannot work on other platforms such as Windows or MacOS or other Python versions.

What it can be guaranteed is that RoundCreator won't work in Python 2.6 due to the argparse dependency.

## Installation
If you have cloned this repo, you can type `python setup.py install`. This will install a package called "RoundCreator" and will create a "RoundCreator" terminal command.

This package can also be installed with pip

`pip install RoundCreator`

You can check [libraries.io](https://libraries.io/pypi/RoundCreator) or [PyPI](https://pypi.org/project/RoundCreator) for the whole version history.

## General overview
RoundCreator accepts some command line arguments and then does some stuff. Its arguments (and its default values) are:
* `--name` Contest name. Its default value is "myContest"
* `--amount` Number of problems. Its default value is 5
* `--single` Type it if you want a single problem. It will place the source and scripts in the contest folder. Overrides `--amount`
* `--author` Your name
* `--command` Shell command to execute after creating the folder structure. Will be execute inside the contest folder. Its default value is `chmod 777 * -R`

## A simple example
Let's suppose that you are competing in a contest called "hardContest" which has two problems (a and b), then, the following command:<br>
`RoundCreator --name hardContest --amount 2`

Will create the following folder structure:

```
$ tree hardContest/
hardContest/
├── a
│   ├── compile.sh
│   └── main.cc
└── b
    ├── compile.sh
    └── main.cc

2 directories, 4 files
```

And, given that the default command changes the permissions of the whole folder structure, you should expect to see something similar to this when listing the files:

```
$ ls -ltRa
.:
total 16
drwxrwxr-x 4 sergiorgs sergiorgs 4096 Aug  8 10:22 .
drwxrwxr-x 3 sergiorgs sergiorgs 4096 Aug  8 10:22 ..
drwxrwxrwx 2 sergiorgs sergiorgs 4096 Aug  8 10:22 a
drwxrwxrwx 2 sergiorgs sergiorgs 4096 Aug  8 10:22 b

./a:
total 16
drwxrwxrwx 2 sergiorgs sergiorgs 4096 Aug  8 10:22 .
drwxrwxr-x 4 sergiorgs sergiorgs 4096 Aug  8 10:22 ..
-rwxrwxrwx 1 sergiorgs sergiorgs  236 Aug  8 10:22 compile.sh
-rwxrwxrwx 1 sergiorgs sergiorgs  342 Aug  8 10:22 main.cc

./b:
total 16
drwxrwxrwx 2 sergiorgs sergiorgs 4096 Aug  8 10:22 .
drwxrwxr-x 4 sergiorgs sergiorgs 4096 Aug  8 10:22 ..
-rwxrwxrwx 1 sergiorgs sergiorgs  236 Aug  8 10:22 compile.sh
-rwxrwxrwx 1 sergiorgs sergiorgs  342 Aug  8 10:22 main.cc
```

## Templates
The code templates are the following:
### C++ source code
```c++
/*
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
```
### Compile script
`g++ main.cc -Wall -Wextra -pedantic -std=c++14 -O2 -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -D_FORTIFY_SOURCE=2 -fsanitize=address -fstack-protector`

### Running on Windows
Since RoundCreator is written in Python you should expect it to work in Windows too. However, there are two unadressed issues:
* The compile script will have the sh extension
* The `--command` flag defaults to a linux command
* Many Windows coders use MinGW instead of gcc. The compile command may not work.
These issues can be addressed by using some sort of unix terminal in windows instead of `cmd.exe` and gcc instead of MinGW.
