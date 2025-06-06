import os
from textnode import TextType, TextNode
from copy_content_from_source import copy_content_from_source


def main():
    source = os.path.join(os.getcwd(), "static") 
    destination = os.path.join(os.getcwd(), "public")
    copy_content_from_source(source, destination)
main()

