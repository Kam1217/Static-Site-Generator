import unittest
from extract_title import extract_title

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_h1_heading(self):
        heading = "# Heading"
        self.assertEqual(extract_title(heading), "Heading")

    def test_h1_not_found_exception(self):
        with self.assertRaises(Exception):
            text = "text with no heading"
            extract_title(text)
