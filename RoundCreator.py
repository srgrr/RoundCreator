'''
    (C) Sergio Rodriguez Guasch 2014-2016 <sergi9rr9r@gmail.com>
'''
import argparse
import shutil
import sys
import os

if sys.platform.startswith('win'):
    scriptSuffix = 'bat'
else:
    scriptSuffix = 'sh'

def createTemplate():
    s = "#include <bits/stdc++.h>\n"
    s+= "using namespace std;\n"
    s+= "\n"
    s+= "int main() {\n"
    s+= "    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);\n\n"
    s+= "}\n"
    open("template.cpp", "w").write(s)

def createCompileScript():
    s = "g++ main.cpp -Wall -O2 -DLOCAL -std=c++11\n"
    open("compile."+scriptSuffix, "w").write(s)

def createTestScript():
    if sys.platform.startswith('win'):
        s = "a.exe < input.txt\n"
    else:
        s = "./a.out < input.txt\n"
    open("test."+scriptSuffix, "w").write(s)

def checkScripts():
    try:
        open("template.cpp", "r")
    except:
        print ("Default template not found:\tcreating template")
        createTemplate()

    try:
        open("compile."+scriptSuffix, "r")
    except:
        print ("Default compile script not found:\tcreating compile")
        createCompileScript()

    try:
        open("test."+scriptSuffix, "r")
    except:
        print ("Default test script not found:\tcreating test")
        createTestScript()

def main():
    checkScripts()
    parser = argparse.ArgumentParser(description='Creates a contest folder structure')
    parser.add_argument("--name", default="myContest", type=str,
                        help="Contest name")
    parser.add_argument("--amount", default=5, type=int,
                        help="Number of problems")
    parser.add_argument("--until", default='e', type=str,
                        help="Letter of last problem")
    parser.add_argument("--template", default="template.cpp", type=str,
                        help="Template file")
    parser.add_argument("--compile", default="compile."+scriptSuffix, type=str,
                        help="Compile script")
    parser.add_argument("--test", default="test."+scriptSuffix, type=str,
                        help="Test script")
    parser.add_argument("--prompt", default=False, type=bool,
                        help="Open a console prompt (Windows only)")
    parser.add_argument("--kinder", default='bueno', type=str,
                        help="Kinder?")
    parser.add_argument("--single", default=False, type=str,
                        help="Folder for a single Problem?")

    args = parser.parse_args()

    problemCount = args.amount
    if args.until.lower() != 'e':
        if len(args.until) != 1:
            raise argparse.ArgumentTypeError("Until must be a single char!")
        if ord(args.until.lower()) < ord('a') or ord(args.until.lower()) > ord('z'):
            raise argparse.ArgumentTypeError("Until must be in [a-zA-Z]!")
        problemCount = ord(args.until.lower()) - ord('a') + 1

    try:
        os.makedirs(args.name)
    except:
        ans = 'a'
        while not ans in ['y', 'n']:
            ans = raw_input("Destination folder already exists, do you want to overwrite it [y|n] ")
            if ans == 'n':
                exit()
            if ans == 'y':
                shutil.rmtree(args.name)
                os.makedirs(args.name)

    if not args.single:
        if problemCount > 26:
            print ("More than 26 problems. Switching to numbers...")
            problemNames = [str(x+1) for x in range(problemCount)]
        else:        
            problemNames = [chr(x + ord('a')) for x in range(problemCount)]
        '''
            For each problem we will copy the following:
            - C++ template
            - compile script
            - test script
            - empty input.txt
            - empty output.txt
        '''
        for problemName in problemNames:
            rootPath = os.path.join(args.name,problemName)
            os.makedirs(rootPath)
            shutil.copy(args.template, os.path.join(rootPath, "main.cpp"))
            shutil.copy(args.compile, os.path.join(rootPath, "compile."+scriptSuffix))
            shutil.copy(args.test, os.path.join(rootPath, "test."+scriptSuffix))
            open(os.path.join(rootPath, "input.txt"), 'w')
            open(os.path.join(rootPath, "output.txt"), 'w')
    else:
        rootPath = args.name
        shutil.copy(args.template, os.path.join(rootPath, "main.cpp"))
        shutil.copy(args.compile, os.path.join(rootPath, "compile."+scriptSuffix))
        shutil.copy(args.test, os.path.join(rootPath, "test."+scriptSuffix))
        open(os.path.join(rootPath, "input.txt"), 'w')
        open(os.path.join(rootPath, "output.txt"), 'w')
        

    print ("Done! Good luck and HAVE FUN!")

    if args.prompt:
        if not 'win' in sys.platform:
            print ('--prompt does NOT work in systems different than Windows!')
        else:
            os.system("start cmd /k")

    if args.kinder.lower() == 'malo':
        os.startfile("https://youtu.be/Z_DyVES7c6w?t=59s")

if __name__ == "__main__":
    main()
