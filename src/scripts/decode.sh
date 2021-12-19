#!/bin/bash

python3 -m venv ../python/venv
source ../python/venv/bin/activate
pip3 install -r ../python/requirements.txt >> /dev/null

python3 ../python/decoder.py ../bin/data.bin
