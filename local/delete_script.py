#!/usr/bin/python3

import os
from os import listdir

ROOT_DIR = "/home/azad/Workspaces/bash_scripts/"
SCRIPT_DICT = {} # SCRIPT_DICT [path_to_script_from_root][name]
DIR_TO_SKIP = ["scripts_archieve"]

def main():

    # Have 2 ways to delete the script
        # 1. Take the script name and search for the script
            # if found, delete
            # if not found, prompt user to find the script via file structure
        # 2. Show user the file structure and make them to find the script and delete
            # Show the available folders and files.
            # Based on user input go deeper until the file is found. 
            # After selecting the file prmpt user to make sure.
            # Have a test mode so that, when it is on, before deleting the script make a backup.
    
    # Get all the available scripts and their path on a data scructure
    rootDirScriptFolders = filterListToSkipFolders(listdir(ROOT_DIR))
    print(rootDirScriptFolders)

    

# end main

def filterListToSkipFolders(listToFilter):
    filteredList = []
    for fileOrDir in listToFilter:
        if isFolder(fileOrDir) and fileOrDir not in DIR_TO_SKIP: 
            filteredList.append(fileOrDir)
        # end if
    # end for
    return filteredList
# end filterListToSkipFolders

def isFolder(fileOrFolder):
    if fileOrFolder != None and "." in fileOrFolder:
        return False
    else:
        return True
# end isFolder

main()
