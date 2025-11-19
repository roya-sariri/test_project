from setuptools import find_packages, setup

with open("requirements.txt") as requirements_file:
    install_reqs = requirements_file.read().splitlines()

setup(
    install_requires=install_reqs,
    name='testpy',
    version='1',
    packages=find_packages(include=[""]),
    url='',
    license='',
    author='sariri',
    author_email='',
    description=''
)
