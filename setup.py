from pathlib import Path

from setuptools import setup, find_packages

install_requires = (Path(__file__).parent / 'requirements.txt').read_text().split('\n')

setup(
    name='pynanto',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
    ],
)
