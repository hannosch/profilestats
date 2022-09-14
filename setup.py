import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

__version__ = '2.1'

setup(
    name='profilestats',
    version=__version__,
    author='Hanno Schlichting',
    author_email='hanno@hannosch.eu',
    url='http://pypi.python.org/pypi/profilestats',
    keywords='profile kcachegrind qcachegrind',
    description='Decorator for profiling individual functions and converting '
                'profiling data to the kcachegrind/qcachegrind format.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    license='BSD',
    install_requires=[
        'pyprof2calltree',
    ],
    py_modules=['profilestats'],
    zip_safe=False,
)
