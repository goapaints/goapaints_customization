from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in goapaints_customization/__init__.py
from goapaints_customization import __version__ as version

setup(
	name="goapaints_customization",
	version=version,
	description="Goa Paints Personal CUstomization",
	author="Raj Tailor",
	author_email="tailorraj111@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
