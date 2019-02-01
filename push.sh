#!/usr/bin/env bash

# Make a commit
git add .
git commit -m "$1"

# Sync and push
./sync.sh
