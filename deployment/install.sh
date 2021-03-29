#!/bin/bash
# install.sh
# Installs the batman door opener project

cd ../

if [ -d "./env" ] 
then
    echo "Virtual environment already exists" 
else
    echo "Setting up python3 virtual environment"
    python -m virtualenv -p python3 env
fi

. env/bin/activate

echo "Installing python requirements"
pip install -r src/requirements.txt
