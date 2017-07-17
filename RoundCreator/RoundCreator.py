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

def template_source():
    s = \
'''#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(0);

}
'''
    return s

def compile_script_source():
    if sys.platform.startswith(''):
        s = ''
    else:
        s = '#!/bin/bash\n'
    s += 'g++ main.cc -Wall -O2 -DLOCAL -std=c++11\n'
    return s

def test_script_source():
    if sys.platform.startswith("win"):
        s = 'a.exe < input.txt\n'
    else:
        s  = '#!/bin/bash\n'
        s += './a.out < input.txt\n'
    return s

def hightail_XML_config(contest_path):
    ret = \
'''<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
<comment>This is the configuration file for Hightail.</comment>
<entry key="pathFromWorkingDirToExec">%%L/a.out</entry>
<entry key="prependingCommand"/>
<entry key="workingDirectory">%s</entry>
<entry key="checkExistence">1</entry>
</properties>
'''%contest_path
    return ret


def main():
    parser = argparse.ArgumentParser(description='Creates a contest folder structure')
    parser.add_argument('--name', default='myContest', type=str,
                        help='Contest name')
    parser.add_argument('--amount', default=5, type=int,
                        help='Number of problems')
    parser.add_argument('--until', default='e', type=str,
                        help='Letter of last problem')
    parser.add_argument('--kinder', default='bueno', type=str,
                        help='Kinder?')
    parser.add_argument('--single', action='store_true',
                        help='Folder for a single Problem?')
    parser.add_argument('--author', default='RoundCreatorUser', type=str,
                        help='Your name!')
    parser.add_argument('--hightail', action='store_true',
                        help='Use hightail?')


    args = parser.parse_args()

    problem_count = args.amount
    until = args.until.lower()
    if until != 'e':
        if len(until) != 1:
            raise argparse.ArgumentTypeError('Until must be a single char!')
        if ord(until) < ord('a') or ord(until) > ord('z'):
            raise argparse.ArgumentTypeError('Until must be in [a-zA-Z]!')
        problem_count = ord(until) - ord('a') + 1

    if os.path.exists(args.name):
        ans = 'a'
        while not ans in ['y', 'n']:
            input_func = raw_input if sys.version_info[0] == 2 else input
            ans = input_func('Destination folder already exists, do you want to overwrite it [y|n] ').lower()
            if ans == 'n':
                exit()
            if ans == 'y':
                shutil.rmtree(args.name)
    os.makedirs(args.name)

    if args.hightail:
        cfgxml = hightail_XML_config(os.path.join(os.getcwd(), args.name))
        open(os.path.join(args.name,'hightail.config'), 'w').write(cfgxml)

    if args.author != 'RoundCreatorUser':
        template = '/*\n Author:    ' + args.author + '\n*/\n' + template_source()
    else:
        template = template_source()
    compiles = compile_script_source()
    tests    = test_script_source()

    if args.amount == 1 or until == 'a':
        args.single = True

    if not args.single:
        if problem_count > 26:
            print('More than 26 problems. Switching to numbers...')
            problem_names = [str(x+1) for x in range(problem_count)]
        else:
            problem_names = [chr(x + ord('a')) for x in range(problem_count)]
    else:
            problem_names = ['']

    for problem_name in problem_names:
        root_path = os.path.join(args.name,problem_name)
        if not args.single:
            os.makedirs(root_path)
        open(os.path.join(root_path, 'main.cc'), 'w').write(template)
        open(os.path.join(root_path, 'compile.'+scriptSuffix), 'w').write(compiles)
        open(os.path.join(root_path, 'test.'+scriptSuffix), 'w').write(tests)
        open(os.path.join(root_path, 'input.txt'), 'w')
        open(os.path.join(root_path, 'output.txt'), 'w')

    print('Done! Good luck and HAVE FUN!')

    if args.kinder.lower() == 'malo':
        import webbrowser
        webbrowser.open('https://youtu.be/Z_DyVES7c6w?t=1m04s')

if __name__ == '__main__':
    main()
