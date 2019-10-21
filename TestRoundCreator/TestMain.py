import unittest
import sys

from TestCommandLine import TestCommandLine
from TestTemplate import TestTemplate
from TestRoundCreator import TestRoundCreator


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCommandLine)
    suite
    .addTest(unittest.TestLoader().loadTestsFromTestCase(TestTemplate))
    suite
    .addTest(unittest.TestLoader().loadTestsFromTestCase(TestRoundCreator))

    success = unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
