from markdown_to_html import markdown_to_html_node 
from htmlnode import *
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path)
    template_file = open(template_path)
    markdown = from_file.read()
    template = template_file.read()

    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    new_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

   

    