#!/bin/bash

# Create venv and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install wheel
pip install -r requirements.txt
echo "Virtual environment created"

# Create tmp dir with problem and solution files inside the directory
DIR_NAME="tmp"
mkdir -p "$DIR_NAME"
touch "$DIR_NAME/problem.txt" "$DIR_NAME/solution.txt"
echo "Directory and files created in $DIR_NAME"