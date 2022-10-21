##### Question 1
pip will install an older version - HEAD in github may have different dependencies (eg econ-ark)

##### Question 2
What do we do w/ stuff like this? (from econ-ark/setup.cfg)

[options.extras_require]
dev =  
    Sphinx
    nbsphinx
    recommonmark
    pre-commit
    seaborn
    networkx
