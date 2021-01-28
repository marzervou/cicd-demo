"""Setup.py script for packaging project."""

from setuptools import setup, find_packages

import yaml
import os


def read_condaenv_dependencies(fname):
    """Get default dependencies from Pipfile.lock."""
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as lockfile:
        lockjson = yaml.load(lockfile, Loader=yaml.FullLoader)
        y = [dependency for dependency in lockjson['dependencies'][16]['pip']]
        return y


if __name__ == '__main__':
    setup(
        name='cicddemo',
        version=os.getenv('PACKAGE_VERSION', '0.0.dev0'),
        package_dir={'': 'src'},
        packages=find_packages(where='src',
                               include=['pack*',]
                               ),
        description='A demo package.',
        install_requires=[
            *read_condaenv_dependencies('environment.yml'),
        ]
    )