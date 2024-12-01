
import os
from os import path

class TestScanner:
    pass

curr_dir = os.getcwd()

def checkTestDir(dirpath : path):
    for root, dirs, files in os.walk(dirpath):  # Walk through the directory tree
        for dir_name in dirs:
            if dir_name in {'tests', 'test'}:  # Check for 'tests' or 'test'
                # return os.path.join(root, dir_name)
                print(True)
    print(False)  # Return None if no matching directory is found


checkTestDir(curr_dir)
