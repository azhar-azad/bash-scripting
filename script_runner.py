#!/usr/bin/python3

from os import listdir
import subprocess

# Global Variables
ROOT_DIR = "/home/azad/Workspaces/bash_scripts/"
SCRIPTS_DICT = {}

def main():

    # Get all scripts name and categorize them
    initScriptsDict()

    # Print all scripts
    printScripts()

    # Get script code from user
    scriptCode = getScriptCode()

    # Run bash scripts based on scriptCode
    runBashScript(scriptCode)
    
# end main


# Get all bash script for the root folder and categorize them
def initScriptsDict():
    rootDirFiles = listdir(ROOT_DIR)

    for fileOrDir in rootDirFiles:
        if isDirectory(fileOrDir):
            if fileOrDir == "estatement":
                estatementDir = ROOT_DIR + fileOrDir
                estatementDirFiles = listdir(estatementDir)
                estmtScriptsList = []
                for f in estatementDirFiles:
                    if isScriptFile(f):
                        estmtScriptsList.append(f)
                    # end if
                # end for 
                SCRIPTS_DICT["E"] = estmtScriptsList
            # end if 

            elif fileOrDir == "local":
                localDir = ROOT_DIR + fileOrDir
                localDirFiles = listdir(localDir)
                localScriptsList = []
                for f in localDirFiles:
                    if isScriptFile(f):
                        localScriptsList.append(f)
                    # end if 
                # end for 
                SCRIPTS_DICT["L"] = localScriptsList
            # end elif 

            # more check for more folders

        # if end
    # for end
# end initScriptsDict 

# Determine if a file or directory is script file or not
def isScriptFile(fileOrDirName):
    if fileOrDirName.find(".sh") != -1 or fileOrDirName.find(".py") != -1:
        return True

    return False
# end isScriptFile 

# Determine if a file or directory is directory or not
def isDirectory(fileOrDirName):
    if fileOrDirName.find(".") == -1:
        return True

    return False
# end isDirectory 

# Print all scripts in a formatted way before getting user input
def printScripts():
    print("ALL SCRIPTS")

    for key in SCRIPTS_DICT.keys():
        if key == "E": 
            print("ESTATEMENT SCRIPTS")
            itemCounter = 1
            for scriptName in SCRIPTS_DICT.get(key):
                print("\t(code = e" + str(itemCounter) + ") " + scriptName)
                itemCounter += 1                
            # end for 
            print("")
        # end if 

        elif key == "L": 
            print("LOCAL SCRIPTS")
            itemCounter = 1
            for scriptName in SCRIPTS_DICT.get(key):
                print("\t(code = l" + str(itemCounter) + ") " + scriptName)
                itemCounter += 1                
            # end for 
            print("")
        # end elif 
    # end for 
# end printScripts 

# Get user input
def getScriptCode():
    scriptCode = input("Which script to run (enter script code): ")
    print(scriptCode)

    try:
        category = scriptCode[0].upper()
        selection = int(scriptCode[1])
    # end try
    except ValueError:
        print("ValueError: Wrong Type. Input again.")
        getScriptCode()
    # end except

    if category not in SCRIPTS_DICT.keys():
        print("CategoryError: Wrong Category. Input again.")
        getScriptCode()
    # end if

    if selection not in range(1, len(SCRIPTS_DICT.get(category)) + 1):
        print("SelectionError: Wrong selection. Input again.")
        getScriptCode()
    # end if

    return scriptCode
# end getScriptCode

# Run bash scripts based on scriptCode
def runBashScript(scriptCode):
    # subprocess.call("test_script.sh")
    category = scriptCode[0].upper()
    scriptIndex = int(scriptCode[1]) - 1
    scriptName = SCRIPTS_DICT[category][scriptIndex]
    if category == "E":
        subprocess.call(ROOT_DIR + "estatement/" + scriptName) 
    # end if
    elif category == "L": 
        subprocess.call(ROOT_DIR + "local/" + scriptName) 
    # end if
# end runBashScript

main()