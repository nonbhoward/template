#!/bin/bash

dir_exist(){
  if [ $# -ne 1 ];then
    echo "function takes one arg, exit" && exit
  else
    if [ -d "$1" ];then
      echo -e "\t$1 exists, continuing"
    else
      echo "$1 not exist, exit" && exit
    fi
  fi
}

execute(){
  echo "$2" && echo -e "\texecuting : $1" && $1
}

file_exist(){
  if [ $# -ne 1 ];then
    echo "function takes one arg, exit" && exit
  else
    if [ -f "$1" ];then
      echo -e "\t$1 exists, continuing"
    else
      echo "$1 not exist, exit" && exit
    fi
  fi
}

