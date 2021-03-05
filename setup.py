import idecomp
from setuptools import setup, find_packages  # type: ignore

long_description = ""
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = []
with open('requirements.txt', 'r') as fh:
    requirements = fh.readlines()

setup(
    name="idecomp",
    version=idecomp.__version__,
    author="Rogerio Alves",
    author_email="rogerioalves.ee@gmail.com",
    description="Interface para arquivos do DECOMP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rjmalves/idecomp",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha"
    ],
    python_requires=">=3.5",
    install_requires=requirements
)
