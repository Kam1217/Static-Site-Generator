import unittest
from blocktype import BlockType, block_to_block_type

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_block_to_heading(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_to_code(self):
        block = "```code```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_quote(self):
        block = ">quote1, >quote2"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_unordered(self):
        block = "- list1, - list2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_ordered(self):
        block = "1. list, 2. list"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_block_to_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    



