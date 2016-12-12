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

def templateSource():
    s = "#include <bits/stdc++.h>\n"
    s+= "using namespace std;\n"
    s+= "\n"
    s+= "int main() {\n"
    s+= "    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);\n\n"
    s+= "}\n"
    return s

def compileScriptSource():
    s = "g++ main.cpp -Wall -O2 -DLOCAL -std=c++11\n"
    return s

def testScriptSource():
    if sys.platform.startswith('win'):
        s = "a.exe < input.txt\n"
    else:
        s = "./a.out < input.txt\n"
    return s

def main():
    parser = argparse.ArgumentParser(description='Creates a contest folder structure')
    parser.add_argument("--name", default="myContest", type=str,
                        help="Contest name")
    parser.add_argument("--amount", default=5, type=int,
                        help="Number of problems")
    parser.add_argument("--until", default='e', type=str,
                        help="Letter of last problem")
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
            ans = raw_input("Destination folder already exists, do you want to overwrite it [y|n] ").lower()
            if ans == 'n':
                exit()
            if ans == 'y':
                shutil.rmtree(args.name)
                os.makedirs(args.name)

    template = templateSource()
    compiles = compileScriptSource()
    tests    = testScriptSource()

    if not args.single:
        if problemCount > 26:
            print ("More than 26 problems. Switching to numbers...")
            problemNames = [str(x+1) for x in range(problemCount)]
        else:        
            problemNames = [chr(x + ord('a')) for x in range(problemCount)]
    else:
            problemNames = ['']
 
    for problemName in problemNames:
        rootPath = os.path.join(args.name,problemName)
        if not args.single: 
            os.makedirs(rootPath)
        open(os.path.join(rootPath, "main.cpp"), 'w').write(template)
        open(os.path.join(rootPath, "compile."+scriptSuffix), 'w').write(compiles)
        open(os.path.join(rootPath, "test."+scriptSuffix), 'w').write(tests)
        open(os.path.join(rootPath, "input.txt"), 'w')
        open(os.path.join(rootPath, "output.txt"), 'w')

    print ("Done! Good luck and HAVE FUN!")

    if args.prompt:
        if not 'win' in sys.platform:
            print ('--prompt does NOT work in systems different than Windows!')
        else:
            os.system("start cmd /k")

    if args.kinder.lower() == 'malo':
	import webbrowser
        webbrowser.open("https://youtu.be/Z_DyVES7c6w?t=1m04s")

if __name__ == "__main__":
    main()
