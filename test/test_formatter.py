import unittest

from app.formatter import Formatter


class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.fm = Formatter()
        self.contents = self.fm.read_file('../data/sample-Liz.in')
        self._entries = self.fm.get_entries_by_line(self.contents)
        self._v_entries = self.fm.validate_entries(self._entries)
        self._format_output = self.fm.format_output()


    def test_read_file_method_returns_correct_type(self):
        self.assertEqual(str, type(self.contents))

    def test_read_file_method_returns_not_empty(self):
        self.assertGreater(len(self.contents), 0)

    def test_get_entries_by_line_method_returns_correct_type(self):
        self.assertEqual(list, type(self._entries))

    def test_line_count_equals_entry_count(self):
        self.assertEqual(self.fm.line_count, self.fm.entry_count)


if __name__ == '__main__':
    unittest.main()
