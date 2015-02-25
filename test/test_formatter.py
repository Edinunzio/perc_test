import unittest
from formatter import Formatter


class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.fm = Formatter()

    def test_read_file_method_returns_correct_type(self):
        self.assertEqual(str, type(self.fm.read_file('../data/sample-Liz.in')))

if __name__ == '__main__':
    unittest.main()
