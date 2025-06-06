import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    contents = os.listdir(dir_path_content)

    for item in contents:
        contents_item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(contents_item_path):
            generate_page(contents_item_path, template_path, dest_dir_path)
        else:
            new_destination = os.path.join(dest_dir_path, item)
            generate_pages_recursive(contents_item_path, template_path, new_destination)