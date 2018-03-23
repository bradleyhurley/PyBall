# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os
from os import path
import versioneer

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'ReadMe.md'), encoding='utf-8') as f:
    long_description = f.read()


dependencies = [
        'requests',
    ]


def package_files(directory):
    """Retuns paths to all files under a directory that are not .pyc"""
    paths = []
    for (file_path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if (not filename.endswith('.pyc') and
                    '.cache' not in filename):
                paths.append(os.path.join('..', file_path, filename))
    return paths



setup(
    name='PyBall',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='A Python 3 Client To Interact with MLB.com Stats ',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/bradleyhurley/PyBall',

    # Author details
    author='Brad Hurley',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: API :: Baseball',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='mlb baseball-statistics baseball-stats mlbam',

    # All source code is under the `supermart` directory so it is easily found
    packages=find_packages(exclude=['test']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=dependencies,

    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'versioneer',
            'codecov',
            'pytest-cov'
        ]
    },

    # This supports adding all the configuration files that are part of our package
    # Note that python packaging documentation is very confusing on this functionality,
    # adding the flag `include_package_data=True` will break this as will adding a
    # MANIFEST.in file
    include_package_data=True,

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
        ],
    },
)