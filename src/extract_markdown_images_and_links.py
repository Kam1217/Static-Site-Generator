import re

def extract_markdown_images(text):

    images_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return images_text

def extract_markdown_links(text):

    link_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return link_text
  