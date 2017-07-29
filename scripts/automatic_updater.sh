#!/bin/bash

set -x

git pull
python scripts/automatic_numbers.py
git add posts/*
git ci -m"Updating to latest numbers automatically"
git push