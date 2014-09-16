#!/usr/bin/env bash

sudo apt-get install -y python-pip
sudo pip install flask
pip freeze > requirements.txt