import re

def extract_markdown_images(text):

    images_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return images_text


  