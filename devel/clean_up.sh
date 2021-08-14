#!/bin/bash

clear && echo "launching clean up script"

# clear data, logs
echo -e "\trm data/*"
rm $(dirname $0)/data/*
echo -e "\trm logs/*"
rm $(dirname $0)/logs/*

