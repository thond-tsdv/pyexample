from setuptools import setup

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name='thond',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/thond-tsdv/pyexample',
    author='Nguyen Dat Tho',
    author_email='tho1.nguyendat@toshiba.co.jp',    
    license='BSD 2-clause',
    long_description=readme,
    long_description_content_type='text/x-rst',
    packages=['thond'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.6',
    ],
)    
