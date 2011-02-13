from setuptools import setup

setup(
    name='profilestats',
    version='1.0.3dev',
    author='Hanno Schlichting',
    author_email='hanno@hannosch.eu',
    url='http://pypi.python.org/pypi/profilestats',
    keywords='profile kcachegrind',
    description='Decorator for profiling individual functions and converting '
                'profiling data to the kcachegrind format.',
    long_description=open("README.txt").read(),
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    license='BSD',
    install_requires=[
        'setuptools',
        'pyprof2calltree',
    ],
    py_modules=['profilestats'],
    zip_safe=False,
)
