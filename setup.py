#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django-inline-ordering',
    version='1.0.1',
    author='Piotr Kilczuk',
    author_email='p.kilczuk@neumea.pl',
    url='http://github.com/centralniak',
    description='Django app to ease ordering of related data - ' \
                'enable Drag&Drop ordering in admin with just a few LOC',
    #packages = ['inline_ordering',],
    packages=find_packages(),
    provides=['inline_ordering',],
    include_package_data=True,
    install_requires=['django-admin-jqueryui==1.0.0', ],
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_data={
        'inline_ordering': [
            'media/inline_ordering.js'
        ],
    },
)
