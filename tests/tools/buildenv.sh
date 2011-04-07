#!/usr/bin/env bash

OLDDIR=`pwd`
SELF=`dirname $0`

cd $SELF/..

if [ "$1" == "--full" ]; then
    rm _oldenv -rf
    mv _env _oldenv
    virtualenv _env --no-site-packages --distribute 
    find /tmp/*.tar.gz -user `whoami` -exec rm {} \;
fi

. _env/bin/activate 
pip install -E _env -r doc/pip-requirements.txt
deactivate 

cd $OLDDIR