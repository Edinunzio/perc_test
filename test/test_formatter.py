"""
Tests for formatter.py
"""

import unittest

from app import formatter


class TestFormatter(unittest.TestCase):
    """
    Formatter test cases
    """

    def setUp(self):
        self.fm = formatter.Formatter()
        self.contents = self.fm.read_file('../data/sample-Liz.in')
        self._entries = self.fm.get_entries_by_line(self.contents)
        self._v_entries = self.fm.validate_entries(self._entries)
        self._format_output = self.fm.format_output()


    def test_read_file_method_returns_correct_type(self):
        """
        tests if read_file returns str
        """
        self.assertEqual(str, type(self.contents))

    def test_read_file_method_returns_not_empty(self):
        """
        tests if read file has content (besides whitespace)
        """
        self.assertGreater(len(self.contents), 0)

    def test_get_entries_by_line_method_returns_correct_type(self):
        """
        tests type of entry container
        """
        self.assertEqual(list, type(self._entries))

    def test_line_count_equals_entry_count(self):
        """
        tests if number of lines in file is equal to number of entries + errors
        """
        self.assertEqual(self.fm.line_count, self.fm.entry_count)


if __name__ == '__main__':
    unittest.main()
