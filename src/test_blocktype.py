import unittest
from blocktype import BlockType, block_to_block_type

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_block_to_heading(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    



