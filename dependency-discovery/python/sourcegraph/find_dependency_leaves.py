from typing import Dict
import argparse
import sys
import os


def _main(argv = None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(argv[0], description = 'Looks in the dir which contains several files with contents à la "package,dependency".' 
    + ' Prints out the packages which have NO dependencies (it does NOT eliminate duplicates)')
    parser.add_argument('dependecyFilesDir', type = str, help = 'Path to the dir containing the dependency files')
    args = parser.parse_args(args = argv[1: ])

    dependencies: Dict[str, set[str]] = {}
    for filename in os.listdir(args.dependecyFilesDir):
        if filename.lower() == 'readme.md':
            continue

        filepath = os.path.join(args.dependecyFilesDir, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    [down, up] = line.split(',')

                    if down not in dependencies:
                        dependencies[down] = set()

                    dependencies[down].add(up.strip())
    
    for dependencySet in dependencies.values():
        for up in dependencySet:
            if up not in dependencies:
                print(up)


if __name__ == '__main__':
    sys.exit(_main())