from setuptools import setup, find_packages
import os
import sys


setup (name='llclusto',
                    version='1.0',
                    description='Provides driver modules', 
                    author='Linden Lab',
                    author_email='lex@lindenlab.com',
                    packages = find_packages('src'),
                    package_dir = {'': 'src'},
                    install_requires = ['clusto',],
                    )
