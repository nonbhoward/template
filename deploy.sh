#!/bin/bash
source "$(dirname "$0")/common/shell.sh"

# definitions
echo "PATH INIT"
CWD=$(dirname "$0")
echo -e "\tCWD=$CWD"
echo -e "\tPWD=$PWD"
path_to_devel="$CWD/devel"
path_to_deploy="$path_to_devel/deploy.py"
path_to_venv="$CWD/venv"
path_to_interpreter="$CWD/venv/bin/python"

## change cwd to script directory
execute "cd $path_to_devel" "CHANGE PWD TO DEVEL"
echo -e "\tCWD=$CWD"
echo -e "\tPWD=$PWD"
## check ./devel exists
dir_exist "$path_to_devel"
## check ./venv exists
dir_exist "$path_to_venv"
## check ./script/main.py exists
file_exist "$path_to_deploy"
## check ./venv/bin/python exists
file_exist "$path_to_interpreter"
# launch python script via python venv interpreter
execute "$path_to_interpreter $path_to_deploy $1" "LAUNCH PYTHON ENVIRONMENT"
exit
