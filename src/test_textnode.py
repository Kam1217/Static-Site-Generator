import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("boot.dev",TextType.LINK, url="https://www.boot.dev/")
        node2 = TextNode("boot.dev",TextType.LINK, url="https://www.boot.dev/")
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("boot.dev",TextType.LINK)
        node2 = TextNode("boot.dev",TextType.LINK, url="https://www.boot.dev/")
        self.assertNotEqual(node, node2)

    def test_diff_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This text is about dogs", TextType.BOLD)
        node2= TextNode("This is a different text about cats", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()