import os, sys, glob
from setuptools import setup
from glob import glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="metric_server",
    version="0.0.1",
    author="Mike Nilson",
    author_email="mike@blacksadhorse.com",
    description="UDP metric server",
    license="BSD",
    keywords="metric",
    url="http://blacksadhorse.com",
    packages=['metric_server'],
    install_requires=[

    ],
    include_package_data=True,
    long_description=read('README'),
    classifiers=[
        "Development Status :: 0 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)