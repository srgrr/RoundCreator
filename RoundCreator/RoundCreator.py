import RoundCreator.CommandLine as CL
import shutil
import sys
import os


def prompt_user_yn(message):
    ans = None
    while ans not in ['y', 'n']:
        print(message)
        ans = input()
    return ans


def create_folder(name):
    if os.path.exists(name):
        print(f'[WARNING]: Folder with name {name} already exists')
        if prompt_user_yn('Do you want to overwrite it? [y/n]') == 'y':
            print(f'Removing old directory {name} and its contents...')
            shutil.rmtree(name)
        else:
            sys.exit(0)
    print(f'Creating directory {name}')
    os.mkdir(name)


def write_to_file(path, content):
    with open(path, 'w') as f:
        f.write(content)


def add_contents_to_folder(name, author, headers='#include <bits/stdc++.h>'):
    import RoundCreator.Template as T
    cpp_template = T.CPP_TEMPLATE.apply({'##AUTHOR##': author, '##HEADERS##': headers})
    compile_script = T.COMPILE_TEMPLATE.apply()

    write_to_file(os.path.join(name, 'main.cc'), cpp_template)
    write_to_file(os.path.join(name, 'compile.sh'), compile_script)


EXHAUSTIVE_HEADERS = """#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cassert>"""


def determine_headers(use_bits_header):
    if use_bits_header:
        return '#include <bits/stdc++.h>'
    return EXHAUSTIVE_HEADERS


def create_contest(name, amount, single, author, command, use_bits_header=False):
    # Create root folder
    create_folder(name)
    if not single:
        for i in range(amount):
            problem_letter = chr(ord('a') + i) if amount <= 26 else str(i)
            problem_path = os.path.join(name, problem_letter)
            create_folder(problem_path)
            add_contents_to_folder(problem_path, author, determine_headers(use_bits_header))
    else:
        add_contents_to_folder(name, author)
    os.system(f'cd {name}; {command}; cd -;')


def main():
    options = CL.parse_arguments()
    create_contest(**vars(options))


if __name__ == '__main__':
    main()
