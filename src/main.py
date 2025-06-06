import os
from textnode import TextType, TextNode
from copy_content_from_source import copy_content_from_source
from generate_pages_recursive import generate_pages_recursive
from generate_page import generate_page


def main():
    source = os.path.join(os.getcwd(), "static") 
    destination = os.path.join(os.getcwd(), "public")
    copy_content_from_source(source, destination)
    generate_pages_recursive("content", "template.html", "public")
    # generate_page("content/index.md", "template.html", "public/index.html")

main()

