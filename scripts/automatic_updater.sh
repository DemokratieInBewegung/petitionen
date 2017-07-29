#!/bin/bash

set -x

git pull
python scripts/update_numbers.py
git add posts/*
git commit -m"Updating to latest numbers automatically"
git push