'''
    (C) Sergio Rodriguez Guasch 2014-2017 <sergi9rr9r@gmail.com>
'''
import argparse
import shutil
import wget
import sys
import os

if sys.platform.startswith("win"):
    scriptSuffix = "bat"
else:
    scriptSuffix = "sh"

def templateSource():
    s = \
"""#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(0);

}
"""
    return s

def compileScriptSource():
    if sys.platform.startswith("win"):
        s = ""
    else:
        s = "#!/bin/bash\n"
    s += "g++ main.cc -Wall -O2 -DLOCAL -std=c++11\n"
    return s

def testScriptSource():
    if sys.platform.startswith("win"):
        s = "a.exe < input.txt\n"
    else:
        s  = "#!/bin/bash\n"
        s += "./a.out < input.txt\n"
    return s

def hightailXMLConfig(contest_path):
    ret = \
"""<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
<comment>This is the configuration file for Hightail.</comment>
<entry key="pathFromWorkingDirToExec">%%L/a.out</entry>
<entry key="prependingCommand"/>
<entry key="workingDirectory">%s</entry>
<entry key="checkExistence">1</entry>
</properties>
"""%contest_path
    return ret


def main():
    parser = argparse.ArgumentParser(description="Creates a contest folder structure")
    parser.add_argument("--name", default="myContest", type=str,
                        help="Contest name")
    parser.add_argument("--amount", default=5, type=int,
                        help="Number of problems")
    parser.add_argument("--until", default="e", type=str,
                        help="Letter of last problem")
    parser.add_argument("--kinder", default="bueno", type=str,
                        help="Kinder?")
    parser.add_argument("--single", default=False, type=str,
                        help="Folder for a single Problem?")
    parser.add_argument("--author", default="RoundCreatorUser", type=str,
                        help="Your name!")
    parser.add_argument("--hightail", default=False, type=str,
                        help="Use hightail?")


    args = parser.parse_args()

    problemCount = args.amount
    until = args.until.lower()
    if until != "e":
        if len(until) != 1:
            raise argparse.ArgumentTypeError("Until must be a single char!")
        if ord(until) < ord("a") or ord(until) > ord("z"):
            raise argparse.ArgumentTypeError("Until must be in [a-zA-Z]!")
        problemCount = ord(until) - ord("a") + 1

    if os.path.exists(args.name):
        ans = "a"
        while not ans in ["y", "n"]:
            input_func = raw_input if sys.version_info[0] == 2 else input
            ans = input_func("Destination folder already exists, do you want to overwrite it [y|n] ").lower()
            if ans == "n":
                exit()
            if ans == "y":
                shutil.rmtree(args.name)
    os.makedirs(args.name)

    if args.hightail:
        cfgxml = hightailXMLConfig(os.path.join(os.getcwd(), args.name))
        open(os.path.join(args.name,'hightail.config'), 'w').write(cfgxml)

    if args.author != "RoundCreatorUser":
        template = "/*\n Author:    " + args.author + "\n*/\n" + templateSource()
    else:
        template = templateSource()
    compiles = compileScriptSource()
    tests    = testScriptSource()

    if args.amount == 1 or until == 'a':
        args.single = True

    if not args.single:
        if problemCount > 26:
            print("More than 26 problems. Switching to numbers...")
            problemNames = [str(x+1) for x in range(problemCount)]
        else:
            problemNames = [chr(x + ord("a")) for x in range(problemCount)]
    else:
            problemNames = [""]

    for problemName in problemNames:
        rootPath = os.path.join(args.name,problemName)
        if not args.single:
            os.makedirs(rootPath)
        open(os.path.join(rootPath, "main.cc"), "w").write(template)
        open(os.path.join(rootPath, "compile."+scriptSuffix), "w").write(compiles)
        open(os.path.join(rootPath, "test."+scriptSuffix), "w").write(tests)
        open(os.path.join(rootPath, "input.txt"), "w")
        open(os.path.join(rootPath, "output.txt"), "w")

    print("Done! Good luck and HAVE FUN!")

    if args.kinder.lower() == "malo":
        import webbrowser
        webbrowser.open("https://youtu.be/Z_DyVES7c6w?t=1m04s")

if __name__ == "__main__":
    main()
