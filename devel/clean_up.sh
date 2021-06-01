#!/bin/bash

# # # local variables
path_script=$PWD

# # # begin script
clear && echo "launching clean up script"
echo "script is running in the directory : $path_script"

# # # get path parts
# IFS, internal field separator
IFS='/' read -ra PARTS <<< "$path_script"
for part in "${PARTS[@]}"; do
  echo "$part"
done

# # # delete logs
# TODO
