#!/usr/bin/env bash

git checkout master
git remote set-url realwiki https://github.com/CIF-Rochester/wiki.wiki.git
git pull realwiki master
git pull origin master
git push origin master
git push realwiki master
