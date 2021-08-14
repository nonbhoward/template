#!/bin/bash
source "$(dirname "$0")/common/shell.sh"

# startup check, defining paths to elements
## announce cwd to user
echo "PATH INIT"
CWD=$(dirname "$0")
echo -e "\tCWD=$CWD"
path_to_script="$CWD/script"
path_to_main="$path_to_script/main.py"
path_to_venv="$CWD/venv"
path_to_interpreter="$CWD/venv/bin/python"

## change cwd to script directory
execute "cd $path_to_script" "CHANGE CWD TO SCRIPT"
echo -e "\tCWD=$CWD"

## check ./script exists
dir_exist "$path_to_script"
## check ./venv exists
dir_exist "$path_to_venv"
## check ./script/main.py exists
file_exist "$path_to_main"
## check ./venv/bin/python exists
file_exist "$path_to_interpreter"
# launch python script via python venv interpreter
execute "$path_to_interpreter $path_to_main" "LAUNCH PYTHON ENVIRONMENT"
