# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in accounts_report_colourpoint/__init__.py
from accounts_report_colourpoint import __version__ as version

setup(
	name='accounts_report_colourpoint',
	version=version,
	description='accounts_report_colourpoint',
	author='craft',
	author_email='shifa@craftinteractive.ae',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
