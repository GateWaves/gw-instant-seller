#!/bin/bash

rm -Rf .venv activate
virtualenv -p python3 .venv
ln -s .venv/bin/activate .
source activate
pip3 install pylint==1.7.4 flask==0.12.2 flask_sqlalchemy==2.3.2 pyblake2==1.1.0 pysha3==1.0.2 requests==2.18.4 \
    pycurve25519==1.0 base58==0.2.5 waitress==1.1.0 simplejson==3.13.2 typing==3.6.2 pycoin==0.80 pywaves==0.8.1
