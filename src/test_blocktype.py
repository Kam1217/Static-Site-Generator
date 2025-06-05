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

        


    



