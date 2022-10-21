from builtins import OSError
import traceback
from typing import Dict, Set
import argparse
import sys
import subprocess


_dependencies: Dict[str, Set] = {}
_toIgnore = set()


def _addDependency(package: str, dependency: str) -> bool:
    '''
        Adds a dependency to the the '_dependencies' map, if it is not there already

        Params
            package - package name
            dep - another package

        Returns
            whether a dependency was added
    '''

    result = False

    if package not in _dependencies:
        _dependencies[package] = set([dependency])

        result = True
    elif dependency not in _dependencies[package]:
        _dependencies[package].add(dependency)

        result = True

    return result


def _resolveDependencies(packageName: str):
    '''
        Populates the '_dependencies' map.

        Params
            packageName - a package name, known to pypi. Cleaned (lower-case, no dashes)

        Returns
            0 if all went well, > 0 if a problem
    '''

    result = 0

    pi = None
    try:
        pi = subprocess.run(['./fetch+print_wheel_direct_dependencies.sh', packageName], capture_output = True, text = True)
        if pi.returncode > 1:
            print(str(pi.stderr), file = sys.stderr)

            result = pi.returncode
        elif pi.returncode == 1:
            _toIgnore.add(packageName)

            result = 0
        else:
            line = ''
            for ch in pi.stdout:
                if ch != '\n':
                    line += ch
                else:
                    spl = line.split(',')
                    if spl[0] not in _toIgnore:
                        added = _addDependency(spl[0], spl[1])
                        if added:
                            rc = _resolveDependencies(spl[1])
                            if rc != 0:
                                break

                    line = ''
    except subprocess.CalledProcessError as exc:
        print(str(pi.stderr), file = sys.stderr)

        result = pi.returncode
    except OSError as exc:
        result = exc.errno
        traceback.print_exc()

    return result


def _main(argv = None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(argv[0], description = 'Given a package name, uses "pip download" to get its "direct" ' +
        'dependencies. Then repeats the process for those until no more dependencies are left. Prints the dependencies (sans versions. Also ' +
        'note that the package name must be "clean"; all lower-case,  no dashes).')
    parser.add_argument('package', type = str, help = 'Path to the METADATA file')
    args = parser.parse_args()

    rc = _resolveDependencies(args.package.lower())
    for package, depSet in _dependencies.items():
        for dep in depSet:
            print(package + ',' + dep)
    
    return rc

if __name__ == '__main__':
    sys.exit(_main())