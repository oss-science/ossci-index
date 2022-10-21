## nteract
Needs to be installed manually/viasnap

## pytables
Manual install

## openjournals
no install

## conda-forge
Only with conda :-)

## openfhe

## openmbee

## SciML

## gdal

## blosc
...a wrapper of C libraries - which have to be installed separately.

## diffqpy
- lists jill as required - pip does not have it
- pip is v1.2.0 - not in github!

## fenics
github...

```
install_requires =
    numpy
    cffi
    setuptools
    fenics-basix >= 0.5.1.dev0, <0.6.0
    fenics-ufl >= 2022.3.0.dev0, <2022.4.0
```

..vs pip

```
(fenics) harrys-mbp-3:numfocus-1 harryst$ pip show fenics
Name: fenics
Version: 2019.1.0
Summary: The FEniCS Project Python Metapackage
Home-page: https://bitbucket.org/fenics-project
Author: The FEniCS Project contributors
Author-email: 
License: 
Location: /Users/harryst/python-venvs/numfocus-1/fenics/lib/python3.8/site-packages
Requires: fenics-dijitso, fenics-ffc, fenics-fiat, fenics-ufl
Required-by: 
(fenics) harrys-mbp-3:numfocus-1 harryst$ pip list
Package        Version
-------------- --------------
fenics         2019.1.0
fenics-dijitso 2019.1.0
fenics-ffc     2019.1.0.post0
fenics-fiat    2019.1.0
fenics-ufl     2019.1.0
mpmath         1.2.1
numpy          1.23.3
pip            22.2.2
setuptools     56.0.0
sympy          1.11.1
```
(not the unknown - to github - version)