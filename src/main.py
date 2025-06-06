import os
from textnode import TextType, TextNode
from copy_content_from_source import copy_content_from_source
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    source = os.path.join(os.getcwd(), "static") 
    destination = os.path.join(os.getcwd(), "public")
    copy_content_from_source(source, destination)
    generate_pages_recursive("content", "template.html", "public", basepath)
    
main()

