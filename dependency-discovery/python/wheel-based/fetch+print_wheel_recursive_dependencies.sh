#!/bin/bash

# Given a list of packages (in a file - one package per line), it prints, for each,
# its dependencies, recursively, in a file (the dir will be deleted + recreated)
#
# Returns
#    0 if all went well
#    1 if the downloaded file is not a wheel file (can happen - eg w/ package typing)

# Input
packageListFile="$1"
outputDir="$2"   # must exist


# Setup part
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


# Work
rm -rf "$outputDir"
mkdir -p "$outputDir"

while read package || [ -n "$package" ]; do
    nohup python3 "$SCRIPT_DIR"/fetch+print_wheel_recursive_dependencies.py $package > "$outputDir"/$package.dependencies 2>&1 &
done < "$packageListFile"

