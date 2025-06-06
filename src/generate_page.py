import os
from markdown_to_html import markdown_to_html_node 
from htmlnode import *
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as from_file, open(template_path) as template_file:
        markdown = from_file.read()
        template = template_file.read()

        html_content = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)

        new_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content).replace('href="/',f'href="{basepath}').replace('src="/',f'src="{basepath}')

    directory = os.path.dirname(dest_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, mode= "w") as page_file:
        page_file.write(new_template)

    