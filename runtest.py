import unittest
from smartpw.rules import LetterFactory, run_factory

__author__ = 'ethan'


class LetterFactoryTest(unittest.TestCase):
    def test_unique(self):
        f1 = LetterFactory()
        f2 = LetterFactory()
        self.assertNotEqual(run_factory(f1, 20), run_factory(f2, 20))

    def test_seed_works(self):
        f1 = LetterFactory(15)
        f2 = LetterFactory(15)
        self.assertEqual(run_factory(f1, 20), run_factory(f2, 20))


if __name__ == '__main__':
    unittest.main()
