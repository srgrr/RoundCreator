----------
RoundCreator
----------
Create a folder structure for programming contest problems. It is intended to work in Python 3. It works and creates appropriate scripts for Windows and Linux.

----------
Installation
----------
If you have downloaded the tar.gz, you can type python3 setup.py install (--user). This will install a package named "RoundCreator". Read the following sections for further explanation.

----------
General overview
----------

RoundCreator accepts the following command line arguments:
* --name Contest name. Its default value is "myContest"
* --amount Number of problems. Its default value is 5
* --single Type it if you want a single problem. It will place the source and scripts in the contest folder. Its default value is False. Overrides amount if specified
* --author Your name. If not specified, it won't appear in your source code template
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
TODO
