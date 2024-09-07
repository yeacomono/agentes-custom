from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in agentes/__init__.py
from agentes import __version__ as version

setup(
	name='agentes',
	version=version,
	description='Module for Agents',
	author='Larael',
	author_email='luisi@overskull.pe',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
