import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_correct(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "target":"_blank"})
        actual = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual, expected)

    def test_repr(self):
        node = HTMLNode(tag = "p", value="Hello World!", children=None, props=None )
        actual = node.__repr__()
        expected = "HTMLNode(tag=p,value=Hello World!,children=None,props=None)"
        self.assertEqual(actual,expected)


