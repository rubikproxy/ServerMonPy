from setuptools import setup, find_packages

# Project metadata
NAME = "ServerMonPy"
VERSION = "0.1.0"
DESCRIPTION = "Real-time server monitoring tool using SSH"
AUTHOR = "sanjay,suresh,logu"
EMAIL = "rubikproxy@gmail.com"
URL = "https://github.com/rubikproxy/ServerMonPy"

# Long description from README file
with open("README.md", "r", encoding="utf-8") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

# List of project dependencies
REQUIREMENTS = [
    "paramiko==2.8.0",
    "psutil==5.8.0",
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ServerMonPy=ServerMonPy.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
    ],
)
