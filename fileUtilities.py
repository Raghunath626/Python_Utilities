import os,shutil,pathlib

def __init__():
    return None

def createDirectory(directoryPath, remove=False):
    """
    Creates a directory in specified path
    If remove is True then it removes all the contents in the existing directory and creates a new oness
    """
    if remove and os.path.exists(directoryPath):
        try:
            shutil.rmtree(directoryPath)
            pathlib.Path(directoryPath).mkdir(parents=True, exist_ok=True)
            # os.mkdir(directory_path)
        except:
            print("Could not remove directory : ", directoryPath)
            return False
    else:
        try:
            pathlib.Path(directoryPath).mkdir(parents=True, exist_ok=True)
            # os.mkdir(directory_path)
        except:
            print("Could not create directory: ", directoryPath)
            return False
        
    return True


def remove_directory(directory_path):
    """
    Removes directory, if directory exists 
    """
    if os.path.exists(directory_path):
        try:
            shutil.rmtree(directory_path)
        except:
            print("Could not remove directory : ", directory_path)
            return False
        
    return True

def clear_directory(directory_path):
    """
    Clears all the files and subdirectories in the specified path
    """
    dirs_files = os.listdir(directory_path)
    
    for item in dirs_files:
        item_path = directory_path+ item
        
        try:
            if os.path.isfile(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path): 
                shutil.rmtree(item_path)
        except Exception as e:
            print(e)
            
    return True

def remove_empty_folders(path, removeRoot=True):
    """
    Removes all empty folders in a directrory
    if removeRoot = True then root directory is also removed if it is empty
    """
    if not os.path.isdir(path):
        return
    
    # remove empty subfolders
    files = os.listdir(path)
    
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            
            if os.path.isdir(fullpath):
                remove_empty_folders(fullpath)

    # if folder empty, delete it
    files = os.listdir(path)
    
    if len(files) == 0 and removeRoot:
        print("Removing empty folder:", path)
        os.rmdir(path)
        
        
def dir_file_count(directory):
    """
    Counts number of files in a directory
    """
    return sum([len(files) for r, d, files in os.walk(directory)])
