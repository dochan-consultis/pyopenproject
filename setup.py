import setuptools
import pathlib

import pkg_resources

VERSION = "0.7.6"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name="pyopenproject",  # Replace with your own username
    version=VERSION,
    author="Alan Padierna Fernández",
    author_email="alanpadierna9595@gmail.com",
    description="Python library to manage OpenProject API endpoints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Flying-Free/python-openproject-api",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
