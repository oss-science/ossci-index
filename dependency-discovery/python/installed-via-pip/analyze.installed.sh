#!/bin/bash

# Reads a directory containing the virtual environments of each package of
# interest, loads said virtual environment, and (recursively) lists all the
# package dependencies therein.

venvDirsLoc="$1"


set -e


# For every virtual environment, list all packages
for d in "$venvDirsLoc"/*; do
    pipInstallProject=$(basename "$d")
    packageName=$(echo $pipInstallProject | cut -d '[' -f 1 | cut -d , -f 1)

    source "$d/bin/activate"

    tmpFile=$(mktemp)
    pip list | grep -v "Package" | grep -v '\-\-\-' | grep -v $packageName | cut -d ' ' -f 1 > "$tmpFile"

    while read -r dependency || [[ -n "$dependency" ]]; do
        echo "$packageName,$dependency"
    done < "$tmpFile"
    
    rm -f "$tmpFile"
    
    deactivate
done 

rm -f "$sciPackageNamesFile"
