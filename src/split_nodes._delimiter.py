from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_node.append(old_node)