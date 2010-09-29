#!/usr/bin/env python

from distutils.core import setup

setup(
    name='inline_ordering',
    version='0.1.0',
    author='Piotr Kilczuk',
    author_email='p.kilczuk@neumea.pl',
    url='http://github.com/centralniak',
    description = 'Django app to ease ordering of related data - ' /
                  'enable Drag&Drop ordering in admin with just a few LOC',
    packages = ['inline_ordering',],
    provides = ['django-inline-ordering (0.1.0)'],
)
