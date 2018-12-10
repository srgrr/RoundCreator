'''
  (C) Sergio Rodriguez Guasch 2014-2018 < sergio dot r dot guasch at gmail dot com >
'''
import argparse
import shutil
import sys
import os

if sys.platform.startswith('win'):
  script_suffix = 'bat'
else:
  script_suffix = 'sh'

def compile_script_source():
  if sys.platform.startswith('win'):
    try:
      import compile_win
    except:
      import RoundCreator.compile_win as compile_win
    return compile_win.source
  try:
    import compile_linux
  except:
    import RoundCreator.compile_linux as compile_linux
  return compile_linux.source

def test_script_source():
  if sys.platform.startswith('win'):
    try:
      import test_win
    except:
      import RoundCreator.test_win as test_win
    return test_win.source
  try:
    import test_linux
  except:
    import RoundCreator.test_linux as test_linux
  return test_linux.source

def template_source():
  try:
    import cpp_template
  except:
    import RoundCreator.cpp_template as cpp_template
  return cpp_template.source

def hightail_XML_config(contest_path):
  try:
    import hightail_config
  except:
    import RoundCreator.hightail_config as hightail_config
  return hightail_config.source % contest_path

def parse_arguments():
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
  parser.add_argument('--command', default='No command',
            help='Command to execute after folder creation (inside contest folder)')
  return parser.parse_args()


def create_folder(name, amount, until, kinder, single, author, hightail, command):
  problem_count = amount
  until = until.lower()
  if until != 'e':
    if len(until) != 1:
      raise argparse.ArgumentTypeError('Until must be a single char!')
    if ord(until) < ord('a') or ord(until) > ord('z'):
      raise argparse.ArgumentTypeError('Until must be in [a-zA-Z]!')
    problem_count = ord(until) - ord('a') + 1

  if os.path.exists(name):
    ans = 'a'
    while not ans in ['y', 'n']:
      input_func = raw_input if sys.version_info[0] == 2 else input
      ans = input_func('Destination folder already exists, do you want to overwrite it [y|n] ').lower()
      if ans == 'n':
        exit()
      if ans == 'y':
        shutil.rmtree(name)
  os.makedirs(name)

  if hightail:
    cfgxml = hightail_XML_config(os.path.join(os.getcwd(), name))
    open(os.path.join(name,'hightail.config'), 'w').write(cfgxml)

  if author != 'RoundCreatorUser':
    template = '/*\n Author:  ' + author + '\n*/\n' + template_source()
  else:
    template = template_source()
  compiles = compile_script_source()
  tests  = test_script_source()

  if amount == 1 or until == 'a':
    single = True
    print('Switching to single due to amount=1 and/or until=\'a\'...')

  if not single:
    if problem_count > 26:
      print('More than 26 problems. Switching to numbers...')
      problem_names = [str(x+1) for x in range(problem_count)]
    else:
      problem_names = [chr(x + ord('a')) for x in range(problem_count)]
  else:
      problem_names = ['']

  for problem_name in problem_names:
    root_path = os.path.join(name,problem_name)
    if not single:
      os.makedirs(root_path)
    open(os.path.join(root_path, 'main.cc'), 'w').write(template)
    open(os.path.join(root_path, 'compile.'+script_suffix), 'w').write(compiles)
    open(os.path.join(root_path, 'test.'+script_suffix), 'w').write(tests)
    open(os.path.join(root_path, 'input.txt'), 'w')
    open(os.path.join(root_path, 'output.txt'), 'w')

  if not sys.platform.startswith('win'):
    os.system('cd %s; chmod 777 * -R' % name)

  print('Done! Good luck and HAVE FUN!')

  if kinder.lower() == 'malo':
    import webbrowser
    webbrowser.open('https://youtu.be/Z_DyVES7c6w?t=1m04s')

  if command != 'No command':
    os.system(command)


def main():
  options = parse_arguments()
  create_folder(**vars(options))
