from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        delimiter_chars = old_node.text.split(delimiter)

        if len(delimiter_chars) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
    
        for i, char in enumerate(delimiter_chars):
            if char == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(char, TextType.TEXT))
            else:
                new_nodes.append(TextNode(char, text_type))

    return new_nodes