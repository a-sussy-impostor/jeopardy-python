from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A package used to create a jeopardy game in python'
LONG_DESCRIPTION = 'This package allows users to create a Jeopardy Game in python quickly.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="jeopardy-python", 
        version=VERSION,
        author="Infinite Infinity",
        author_email="<randominfiniteinfinity@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],      
        keywords=['python', 'package', 'game', 'jeopardy'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Any",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
