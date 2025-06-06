import os
import shutil

def copy_content_from_source(source, destination):

    if not os.path.exists(source):
        raise Exception(f"{source} directory does not exist!")

    if os.path.exists(destination):
       shutil.rmtree(destination)
    os.mkdir(destination) 

    contents = os.listdir(source)
    
    for item in contents:
        source_item_path = os.path.join(source, item)
        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, destination)
        else:
            new_destination = os.path.join(destination, item)
            copy_content_from_source(source_item_path,new_destination)
   