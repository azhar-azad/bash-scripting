#!/bin/bash

# Create a new script

echo "CREATE_SCRIPT.sh"
echo

# Read the script name
echo "Enter the scripts name with extension: "
read script_name

# Read the folder name where new script will go
echo "Enter the folder name in which the script will go: "
echo "--> estatement"
echo "--> local"
read folder_name

# Change directory to bash_scripts folder
cd "/home/azad/Workspaces/bash_scripts/$folder_name"

# Create the script file
touch $script_name

# Make the file executable
sudo chmod +x $script_name

# Open the script file in vscode
code $script_name