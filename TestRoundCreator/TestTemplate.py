import unittest
import RoundCreator.Template as T


class TestTemplate(unittest.TestCase):

    def testTemplate_NoSubst_OK(self):
        t = T.Template('Hello!')
        self.assertEqual(t.apply(), 'Hello!')

    def testTemplate_Subst_OK(self):
        t = T.Template('Hello ##PERSON##!')
        self.assertEqual(t.apply({'##PERSON##': 'Sergio'}), 'Hello Sergio!')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
