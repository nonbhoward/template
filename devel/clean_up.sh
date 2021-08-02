#!/bin/bash

clear && echo "launching clean up script"
echo "script is running in the directory : $PWD"

# clear data, logs
echo -e "\trm data/*"
rm data/*
echo -e "\trm logs/*"
rm logs/*

