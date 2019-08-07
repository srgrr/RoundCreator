'''
  (C) Sergio Rodriguez Guasch 2014-2019 < sergio dot r dot guasch at gmail dot com >
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


def create_folder(name, amount, single, author, command):
  pass

def main():
  import RoundCreator.CommandLine as CL
  options = CL.parse_arguments()
  create_folder(**vars(options))
