import unittest

from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextNode, TextType

class TestParentNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value,"This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("print(This is code written in python)", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print(This is code written in python)")

    def test_link(self):
        node = TextNode("Click me! - This is a link", TextType.LINK, url="https://www.boot.dev/") 
        html_node= text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value,"Click me! - This is a link")
        self.assertDictEqual(html_node.props, {"href":"https://www.boot.dev/"})

    def test_image(self):
        node = TextNode("Ducks",TextType.IMAGE, url="https://images.pexels.com/photos/132464/pexels-photo-132464.jpeg") 
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"https://images.pexels.com/photos/132464/pexels-photo-132464.jpeg", "alt":"Ducks"})