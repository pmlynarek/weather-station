#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()


with open(
    path.join(path.dirname(path.abspath(__file__)), "requirements.txt")
) as requirement_file:
    requirements = requirement_file.read().split("/n")

setup_requirements = ["pytest-runner"]

with open(
    path.join(path.dirname(path.abspath(__file__)), "requirements-dev.txt")
) as dev_requirement_file:
    test_requirements = dev_requirement_file.read().split("/n")

setup(
    author="Patryk Młynarek",
    author_email="pmlynarek1@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description="weather",
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="weather",
    name="weather",
    packages=find_packages(include=["weather"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/pmlynarek/weather",
    version="0.1.0",
    zip_safe=True,
)
