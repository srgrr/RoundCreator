import unittest
import RoundCreator.CommandLine as CL
import sys
from argparse import ArgumentTypeError


class TestCommandLine(unittest.TestCase):

    def setUp(self):
        self.old_sys_argv = sys.argv

    def tearDown(self):
        sys.argv = self.old_sys_argv

    def testCommandLine_DefaultArgs_OK(self):
        sys.argv = 'RoundCreator'.split(' ')
        options = CL.parse_arguments()
        self.assertEqual(options.name, CL.DEFAULTS.NAME)
        self.assertEqual(options.amount, CL.DEFAULTS.AMOUNT)
        self.assertEqual(options.single, CL.DEFAULTS.SINGLE)
        self.assertEqual(options.author, CL.DEFAULTS.AUTHOR)
        self.assertEqual(options.command, CL.DEFAULTS.COMMAND)

    def testCommandLine_SpecificName_OK(self):
        sys.argv = 'RoundCreator --name specialName'.split(' ')
        options = CL.parse_arguments()
        self.assertEqual(options.name, 'specialName')
        self.assertEqual(options.amount, CL.DEFAULTS.AMOUNT)
        self.assertEqual(options.single, CL.DEFAULTS.SINGLE)
        self.assertEqual(options.author, CL.DEFAULTS.AUTHOR)
        self.assertEqual(options.command, CL.DEFAULTS.COMMAND)

    def testCommandLine_SpecificAmount_OK(self):
        sys.argv = 'RoundCreator --amount 5'.split(' ')
        options = CL.parse_arguments()
        self.assertEqual(options.name, CL.DEFAULTS.NAME)
        self.assertEqual(options.amount, 5)
        self.assertEqual(options.single, CL.DEFAULTS.SINGLE)
        self.assertEqual(options.author, CL.DEFAULTS.AUTHOR)
        self.assertEqual(options.command, CL.DEFAULTS.COMMAND)

    def testCommandLine_NullAmount_ArgumentTypeError(self):
        sys.argv = 'RoundCreator --amount 0'.split(' ')
        with self.assertRaises(ArgumentTypeError):
            CL.parse_arguments()

    def testCommandLine_NegativeAmount_ArgumentTypeError(self):
        sys.argv = 'RoundCreator --amount -1'.split(' ')
        with self.assertRaises(ArgumentTypeError):
            CL.parse_arguments()

    def testCommandLine_CorrectAuthor_OK(self):
        sys.argv = 'RoundCreator --author sergioRG'.split(' ')
        options = CL.parse_arguments()
        self.assertEqual(options.name, CL.DEFAULTS.NAME)
        self.assertEqual(options.amount, CL.DEFAULTS.AMOUNT)
        self.assertEqual(options.single, CL.DEFAULTS.SINGLE)
        self.assertEqual(options.author, 'sergioRG')
        self.assertEqual(options.command, CL.DEFAULTS.COMMAND)

    def testCommandLine_CheatingAuthor_ArgumentTypeError(self):
        sys.argv = 'RoundCreator --author */'.split(' ')
        with self.assertRaises(ArgumentTypeError):
            CL.parse_arguments()

    def testCommandLine_FullSpec_OK(self):
        sys.argv =\
            (
                'RoundCreator -n HardContest --amount 5 '
                '--author sergioRG --command'
            ).split(' ') + ['chmod 777 * -R']
        options = CL.parse_arguments()
        self.assertEqual(options.name, 'HardContest')
        self.assertEqual(options.amount, 5)
        self.assertEqual(options.single, CL.DEFAULTS.SINGLE)
        self.assertEqual(options.author, 'sergioRG')
        self.assertEqual(options.command, 'chmod 777 * -R')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCommandLine)
    unittest.TextTestRunner(verbosity=2).run(suite)
