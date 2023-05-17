from ceasar import __version__

with open("README.md", "r") as fh:
    description = fh.read()

scripts = ["bin/ceasar"]

setup_args = {
    "name": "ceasar",
    "version": __version__,
    "url": "https://github.com/toshydev/ceasar",
    "description": "A Ceasar cipher ROT13 tool",
    "long_description": description,
    "long_description_content_type": "text/markdown",
    "author": "Anton Roters",
    "author_email": "antonroters@hotmail.com",
    "license": "MIT",
    "packages": ["ceasar"],
    "scripts": ["bin/ceasar"],
    "include_package_data": True,
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Topic :: Security :: Cryptography",
    ]
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**setup_args)
