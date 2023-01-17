#!/usr/bin/env python

from setuptools import find_packages, setup  # type: ignore

setup(
    name="verify-x509",
    url="https://github.com/pyauth/verify-x509",
    project_urls={
        "Documentation": "https://pyauth.github.io/verify-x509/",
        "Change log": "https://github.com/pyauth/verify-x509/blob/main/Changes.rst",
        "Issue tracker": "https://github.com/pyauth/verify-x509/issues",
    },
    license="Apache Software License",
    author="Andrey Kislyuk",
    author_email="kislyuk@gmail.com",
    description="A minimalistic X.509 certificate validator",
    long_description=open("README.rst").read(),
    use_scm_version={
        "write_to": "verify_x509/version.py",
    },
    setup_requires=["setuptools_scm >= 3.4.3"],
    install_requires=["cryptography >= 40.0"],
    extras_require={
        "tests": [
            "flake8",
            "coverage",
            "build",
            "wheel",
            "mypy",
        ]
    },
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    package_data={
        "verify_x509": ["py.typed"],
    },
    platforms=["MacOS X", "Posix"],
    test_suite="test",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
