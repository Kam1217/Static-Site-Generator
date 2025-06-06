import os
import shutil

def copy_content_from_source(source, destination):

    if not os.path.exists(source):
        raise Exception(f"{source} directory does not exist!")

    if os.path.exists(destination):
       shutil.rmtree(destination)
    os.mkdir(destination) 

    contents = os.listdir(source)
    print(contents)
   