import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_raise_error_no_tag(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode("",[child_node])
            parent_node.to_html()

    def test_raise_error_no_child(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("p",[])
            parent_node.to_html()