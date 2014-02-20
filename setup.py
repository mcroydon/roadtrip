try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="roadtrip",
    version="0.2.4",
    description="Route53 domain updates for humans.",
    author="Matt Croydon",
    author_email="mcroydon@gmail.com",
    long_description=open("README.rst", "r").read(),
    url="https://github.com/mcroydon/roadtrip",
    scripts=["roadtrip"],
    license="BSD",
    install_requires=["boto>=2.25.0"],
    classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2"
    ],
)
