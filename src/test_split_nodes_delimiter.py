import unittest
from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_bold_delimiter(self):
        old_node = TextNode("This is a **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic_delimiter(self):
        old_node = TextNode("This is an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)


