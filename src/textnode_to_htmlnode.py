from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
