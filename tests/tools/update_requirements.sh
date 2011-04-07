#!/usr/bin/env bash

OLDDIR=`pwd`
SELF=`dirname $0`

cd $SELF

pip freeze -E ../_env > ../doc/pip-requirements.txt

cat ../doc/pip-requirements.txt

cd $OLDDIR
