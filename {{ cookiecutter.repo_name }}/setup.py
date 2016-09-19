from setuptools import setup, find_packages
# To use a consistent encoding
from os import path
import versioneer

here = path.abspath(path.dirname(__file__))

setup(
    name="{{ cookiecutter.project_name }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='',
    long_description='',

    # Author details
    author='Tom Augspurger',
    author_email='tom.w.augspurger@gmail.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='data analysis',
    packages=find_packages(exclude=['tests']),
    extras_require={
        'dev': ['cython', 'numpydoc'],
        'test': ['coverage', 'pytest'],
    },
    entry_points="""
        [console_scripts]
        {{ cookiecutter.project_name }}={{ cookiecutter.project_name }}.cli:cli
    """
)
