import unittest
from formatter import Formatter


class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.fm = Formatter()
        self.contents = self.fm.read_file('../data/sample-Liz.in')

    def test_read_file_method_returns_correct_type(self):
        self.assertEqual(str, type(self.contents))

    def test_read_file_method_returns_not_empty(self):
        self.assertGreater(len(self.contents), 0)

    def test_get_entries_by_line_method_returns_correct_type(self):
        self.assertEqual(list, type(self.fm.get_entries_by_line(self.contents)))
if __name__ == '__main__':
    unittest.main()
