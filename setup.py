# setup.py
import cli_pretty_table.cli_pretty_table
from setuptools import setup, find_packages

setup(
    name='cli_pretty_table',
    version='0.0.1',
    packages=find_packages(include=['cli_pretty_table', 'exampleproject.*']),
    install_requires=[
        'texttable==1.6.4',
    ]
)
