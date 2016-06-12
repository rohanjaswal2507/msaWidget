#Python Script to install the MSA Widget
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

#readme = open('README.md').read()
#history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='msaWidget',
    version='0.1.0',
    description='IPython widget for biojs',
    #long_description=readme + '\n\n' + history,
    author='Rohan Jaswal',
    author_email='rohanjaswal2507@gmail.com',
    #url='https://github.com/petrushy/CesiumWidget',
    packages=['msaWidget'],
    install_requires=['ipywidgets'],
    include_package_data=True,
    license="Apache",
    zip_safe=False,
    keywords='msaWidget ipython jupyter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
