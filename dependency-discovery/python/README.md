This is the first attempt at resolving package dependencies in python.

We start with packages that are "pip-compliant". Ideally we can look at their git repos, see where they are following the appropriate _PEP_ conventions and, either
1. create a parser thereof, or
2. use the existing one, that ships with _pip_.

Wanted to do 2., but it is rather difficult - the code included in the _pip_ package, is a mess (no clean API - _pip_ is a cmd line utility, after all + does not provide an API); would "probably" have to modify said code to use it as a library. 

The lowest-hanging-fruit is to use the _pip download_ command - the downloaded package, <u>if it is a wheel</u>, has a fairly simple format, which we can use (essentially all the stuff we care about goes into a file called _METADATA_). So decided to go that route first.

The subdirectories are as follows

- ___installed-via-pip___ - contains code to analyze dependencies for packages that have been already 'installed'
- ___wheel-based___ - scripts to find dependencies of packages that have been uploaded to _pypi_ (as _wheels_).
- ___sourcegraph___ - scripts that use the sourcegraph API/CLI
- ___numfocus-1.data___ - contains info from repos that we got from _numfocus_.