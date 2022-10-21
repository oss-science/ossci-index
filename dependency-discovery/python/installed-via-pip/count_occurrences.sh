#/bin/bash

# Counts the occurrences of the dependent packages

pipListFile="$1"


dependenciesFile=$(mktemp)
uniqDependenciesFile=$(mktemp)
cat "$pipListFile" | cut -d , -f 2 > "$dependenciesFile"

sort -u "$dependenciesFile" > "$uniqDependenciesFile"

while read -r dep || [[ -n "$dep" ]]; do
    cnt=$(grep -c "$dep" "$dependenciesFile")
    echo $dep,$cnt
done < "$uniqDependenciesFile"

rm -f "$dependenciesFile" "$uniqDependenciesFile"
