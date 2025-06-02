import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This text is about dogs", TextType.BOLD)
        node2= TextNode("This is a different text about cats", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_empty_url(self):
        node = TextNode("", TextType.LINK)


if __name__ == "__main__":
    unittest.main()