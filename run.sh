#!/bin/bash

if [ -d "./env" ]; then
	echo "Virtual env already exists"
	source ./env/bin/activate
else
	echo "Creating virtual env..."
	python3 -m venv env
	source ./env/bin/activate
	pip install -r requirements.txt
fi

echo 'Running...'
python3 main.py
