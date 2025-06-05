from splitnodesdelimiter import split_nodes_delimiter
from splitnodesimagesandlinks import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    nodes = []

    text_node = TextNode(text, TextType.TEXT)
    nodes.append(text_node)

    bold_text = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    italic_text = split_nodes_delimiter(bold_text, "_", TextType.ITALIC)
    code_text = split_nodes_delimiter(italic_text, "`", TextType.CODE)
    image = split_nodes_image(code_text) 
    final = split_nodes_link(image)

    return final