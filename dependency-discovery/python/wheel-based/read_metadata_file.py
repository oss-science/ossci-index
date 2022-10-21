import argparse
import sys


def _getCleanPackageName(requiresDistLine: str):
    '''
        Params
            requiresDistLine  - a  'Requires-Dist:' line  the METADATA fiole

        Returns
            the package name, cleaned (lowercase, no dashes)
    '''

    requirement = requiresDistLine.split(': ')[1].strip()
    endOfPackageName = 100000

    for i in range(len(requirement)):
        ch = requirement[i]
        if ch.isalnum() is False and ch not in ('-', '_', '.'):
            endOfPackageName = i

            break

    return requirement[:endOfPackageName].replace('-', '_').lower()

    
def _main(argv = None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(argv[0], description = 'Reads the METADATA file that gets downloaded via ' +
        '"pip download" + "unzip <wheel>: and prints, to stdout, the first set of dependencies. Does this by ' +
        'reading top-to-bottom what is on the right side of "Requires-Dist:". Stops printing after it encounters ' +
        'the first line starting with something other than "Requires-Dist:". Does not print versions')
    parser.add_argument('metadataFile', type = str, help = 'Path to the METADATA file')
    args = parser.parse_args()

    with open(args.metadataFile) as f:
        lines = f.readlines()
    
        requiresDistFirstBlockEnd = None
        for line in lines:
            if requiresDistFirstBlockEnd in (None, False):
                if line.strip().startswith('Requires-Dist:'):
                    requiresDistFirstBlockEnd = False
                    requirement = _getCleanPackageName(line)

                    print(requirement)
                elif requiresDistFirstBlockEnd is False:
                    requiresDistFirstBlockEnd = True

                    break


if __name__ == '__main__':
    sys.exit(_main())