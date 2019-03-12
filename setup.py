import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as fp:
    long_description = fp.read()

setup(
    name="attribute-mapping",
    description="minimal attrdict implementation",
    long_description=long_description,
    version="1.2.0",
    author="wouter bolsterlee",
    author_email="wouter@bolsterl.ee",
    url="https://github.com/wbolster/attribute-mapping",
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    py_modules=["attribute_mapping"],
)
