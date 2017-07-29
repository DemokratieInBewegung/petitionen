#!/bin/bash

set -x

git pull
python3 scripts/update_numbers.py
git add posts/*
git commit -m"Updating to latest numbers automatically"
git push