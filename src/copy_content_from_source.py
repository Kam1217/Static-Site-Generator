import os

def copy_content_from_source():
    # os.path.exists - Return True if path refers to an existing path or an open file descriptor. 
    # os.listdir - Return a list containing the names of the entries in the directory given by path
    # os.path.join - Join one or more path segments intelligently.
    # os.path.isfile - Return True if path is an existing regular file.
    # os.mkdir - Create a directory named path with numeric mode mode. - It is also possible to create temporary directories; see the tempfile module’s tempfile.mkdtemp() function.
    # shutil.copy - Copies the file src to the file or directory dst. src and dst should be path-like objects or strings
    # shutil.rmtree - Delete an entire directory tree; path must point to a directory (but not a symbolic link to a directory)

    # Go into the public directory and check for any files 
    # If files exist delete them - this ensures the copy is clean 
    # Once public is empty of files we can copy some over
    # Go into static directory and check for files 
    # Copy files (including nested directories)
    # Place copied files into public
    # Log the path of each file copy- helps with debugging 


    #STEP 1 = first delete all the contents of the destination directory (public) to ensure that the copy is clean.
    #os.path.join - make path to public intelligently - use os.getcwd() to make it work for any machine 
    #os.path.exists - check public exists - if not make it with os.mkdir
    #osshutil.rmtree if exists to remove all contents 
    # make a new one with os.mkdir once deleted
    
    