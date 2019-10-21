import unittest
import RoundCreator.RoundCreator as RC
import sys


class TestRoundCreator(unittest.TestCase):
    CONTEST_NAME = 'hardContest'
    CONTEST_AMOUNT = 2
    CONTEST_SINGLE = False
    CONTEST_AUTHOR = 'TestAuthor'
    CONTEST_COMMAND = 'chmod 777 * -R'

    def setUp(self):
        pass

    def tearDown(self):
        import shutil
        try:
            shutil.rmtree(self.CONTEST_NAME)
        except Exception as e:
            pass

    def testRoundCreatorCreateContest_HardContest2Problems_OK(self):
        RC.create_contest(
            self.CONTEST_NAME,
            self.CONTEST_AMOUNT,
            self.CONTEST_SINGLE,
            self.CONTEST_AUTHOR,
            self.CONTEST_COMMAND)
        import os
        self.assertTrue(os.path.exists(self.CONTEST_NAME))
        import glob
        inside_items =\
            list(sorted(glob.glob(os.path.join(self.CONTEST_NAME, '*'))))
        problems = [os.path.join(self.CONTEST_NAME, x) for x in ['a', 'b']]
        self.assertEquals(inside_items, problems)

        for problem in problems:
            cc_source = os.path.join(problem, 'main.cc')
            compile_script = os.path.join(problem, 'compile.sh')
            inside_items = list(sorted(glob.glob(os.path.join(problem, '*'))))
            self.assertEquals(inside_items, [compile_script, cc_source])
