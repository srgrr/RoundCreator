from argparse import ArgumentParser, ArgumentTypeError

class DEFAULTS:
  NAME    = "myContest"
  AMOUNT  = 5
  SINGLE  = False
  AUTHOR  = "Da best coder!"
  COMMAND = "chmod 777 * -R"

def _get_parser():
  parser  =  ArgumentParser(
    description = "Creates a contest folder structure"
    )

  # Name of the contest folder
  # Should be a valid UNIX file path
  parser.add_argument(
    "-n",
    "--name",
    default = DEFAULTS.NAME,
    type = str,
    help = "Contest name"
  )

  # Number of problems of this contest
  # amount >= 1
  parser.add_argument(
    "-a",
    "--amount",
    default = DEFAULTS.AMOUNT,
    type = int,
    help = "Number of problems"
    )

  # Equivalent to --amount 1
  # But will place all the source directly inside the folder
  # --single overrides --amount
  parser.add_argument(
    "-s",
    "--single",
    action = "store_true",
    help = "Folder for a single Problem?"
  )

  # Author name. Will appear in the top of the source code if specified
  parser.add_argument(
    "--author",
    default = DEFAULTS.AUTHOR,
    type = str,
    help = "Your name!"
  )

  # Add some command to execute after the folder creation
  parser.add_argument(
    "-c",
    "--command",
    default = DEFAULTS.COMMAND,
    help = "Command to execute after folder creation (inside contest folder)"
  )

  return parser

def _check_name(name):
  import re
  # This regex filters non-valid filenames in POSIX-compliant systems
  invalid_filename_regex = re.compile(r"[^-_.A-Za-z0-9]")
  if invalid_filename_regex.match(name):
    raise ArgumentTypeError("Name is not a valid file path (received %s)" % name)

def _check_amount(amount):
  if amount < 1:
    raise ArgumentTypeError("Amount is zero or negative (received %d)" % amount)

def _check_author(author):
  if author is not None:
    import re
    invalid_author_regex = re.compile(r".*(\*\/)+.*")
    if invalid_author_regex.match(author):
      raise ArgumentTypeError("Author contains */, it may produce an invalid code template (received %s)" % author)

def _check_arguments(options):
  _check_name(options.name)
  _check_amount(options.amount)
  _check_author(options.author)

def parse_arguments():
  ret =  _get_parser().parse_args()
  _check_arguments(ret)
  return ret