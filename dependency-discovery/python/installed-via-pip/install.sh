#!/bin/bash

# Reads a file containing the packages to be tested; creates a virtual
# environment for each, and it installs it therein (via pip install - with its
# dependencies)

venvDirsLoc="$1"
projectListFile="$2"


set -e


while read -r projectList || [[ -n "$projectList" ]]; do
    rm -rf "$venvDirsLoc/$projectList"
    
    python3 -m venv "$venvDirsLoc/$projectList"
    source "$venvDirsLoc/$projectList/bin/activate"
    python3 -m pip install --upgrade pip

    while IFS=',' read -ra packageArr; do
        for packageName in "${packageArr[@]}"; do
            pip install $packageName
        done
    done <<< "$projectList"
    
    deactivate
done < "$projectListFile"    
