from extract_markdown_images_and_links import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        extracted_imgs = extract_markdown_images(original_text)
        
        if len(extracted_imgs) == 0:
            new_nodes.append(old_node)
            continue

        for image in extracted_imgs:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) !=2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        extracted_links = extract_markdown_links(original_text)

        if len(extracted_links) == 0:
            new_nodes.append(old_node)
            continue 

        for link in extracted_links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) !=2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes