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

    def test_code_delimiter(self):
        old_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_unclosed_delimiter_raises_error(self):
        old_node = TextNode("This has **unclosed bold text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([old_node], "**", TextType.BOLD)

    def test_multiple_delimiters(self):
        old_node = TextNode("Start **bold1** middle **bold2** end", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("bold1", TextType.BOLD),
            TextNode(" middle ", TextType.TEXT),
            TextNode("bold2", TextType.BOLD),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_various_delimiters(self):
        old_node = TextNode("Mix of **bold**, _italic_, and `code` here", TextType.TEXT)
    
  
        bold = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(italic, "`", TextType.CODE)
    
        expected = [
            TextNode("Mix of ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_first_word_delimiters(self):
        old_node = TextNode("**Bold** first word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" first word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes,expected)