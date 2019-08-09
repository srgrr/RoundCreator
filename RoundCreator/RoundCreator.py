import argparse
import shutil
import sys
import os

def prompt_user_yn(message):
  ans = None
  while ans not in ["y", "n"]:
    print(message)
    ans = input()
  return ans

def create_folder(name):
  if os.path.exists(name):
    print("[WARNING]: Folder with name %s already exists" % name)
    if prompt_user_yn("Do you want to overwrite it? [y/n]") == "y":
      print("Removing old directory %s and its contents..." % name)
      shutil.rmtree(name)
    else:
      sys.exit(0)
  print("Creating directory %s" % name)
  os.mkdir(name)

def write_to_file(path, content):
  with open(path, "w") as f:
    f.write(content)

def add_contents_to_folder(name, author):
  import RoundCreator.Template as T
  cpp_template = T.CPP_TEMPLATE.apply({"##AUTHOR##": author})
  compile_script = T.COMPILE_TEMPLATE.apply()

  write_to_file(os.path.join(name, "main.cc"), cpp_template)
  write_to_file(os.path.join(name, "compile.sh"), compile_script)


def create_contest(name, amount, single, author, command):
  # Create root folder
  create_folder(name)
  if not single:
    for i in range(amount):
      problem_letter = chr(ord('a') + i) if amount <= 26 else str(i)
      problem_path = os.path.join(name, problem_letter)
      create_folder(problem_path)
      add_contents_to_folder(problem_path, author)  
  else:
    add_contents_to_folder(name, author)
  os.system("cd %s; %s; cd -;" % (name, command))


def main():
  import RoundCreator.CommandLine as CL
  options = CL.parse_arguments()
  create_contest(**vars(options))


if __name__ == "__main__":
  main()
