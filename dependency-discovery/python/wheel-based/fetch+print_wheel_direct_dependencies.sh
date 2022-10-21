#!/bin/bash

# Downloads the package from pypi, and prints the dependencies (direct only) from
# the METADATA file
#
# Returns
#    0 if all went well
#    1 if the downloaded file is not a wheel file (can happen - eg w/ package typing)

package="$1"


set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


tmpDir=$(mktemp -d)
pip download -d "$tmpDir" --no-deps $package > /dev/null 2>&1
for f in "$tmpDir/"*; do
    if [[ "$f" == *.whl ]]; then
        unzip -d "$tmpDir" "$f" > /dev/null 2>&1

        for f in "$tmpDir/"*dist-info"/METADATA"; do
            depTmpFile=$(mktemp)

            python3 "$SCRIPT_DIR"/read_metadata_file.py "$f" > "$depTmpFile"
            while IFS= read -r line; do
                echo $package,"$line" | tr -d '(' | tr -d ')' | sed 's/\ /,/'
            done < "$depTmpFile"

            rm -f "$depTmpFile"
        done
    else
        exit 1
    fi
done

rm -rf "$tmpDir"
