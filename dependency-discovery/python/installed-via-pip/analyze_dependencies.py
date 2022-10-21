from pip._internal.pyproject import load_pyproject_toml, BuildSystemDetails
import argparse
import sys
import os


def _main(argv = None):
    '''
        All args via argparse.
    '''

    if argv == None:
        argv = sys.argv

    parser = argparse.ArgumentParser(argv[0], description = 'Finds the dependencies of a package, based on the config file contents')
    parser.add_argument('configFile', type = str, help = 'Path to the config file that describes what/how should be mentioned (json file))')
    args = parser.parse_args(args = argv[1: ])
    
    if os.path.isfile(args.configFile):
        if os.path.basename(args.configFile) == 'pyproject.toml':
            sd = load_pyproject_toml(None, args.configFile)

            pass
   

if __name__ == '__main__':
    sys.exit(_main())