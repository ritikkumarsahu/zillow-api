from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    
    name='zillow_api',
    version='2.0.0',
    description='Zillow api is scrapper for the [Zillow](https://zillow.com) which fetches the addresses for every US State.'
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ritik Kumar Sahu', 
    author_email='ritikrks@gmail.com', 

    packages=find_packages(where='src'),  # Required
    python_requires='>=3.5, <4',

    install_requires=parse_requirements('requirements.txt', session='hack')

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'run=run:main',
        ],
    },
)
