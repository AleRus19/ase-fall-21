#!/usr/bin/env bash
#
# ASE Flask skeleton script
#
set -e

# export the variables for flask
export FLASK_ENV=development
export FLASK_DEBUG=0
export FLASK_APP=myservice

# execute the flask run command
flask run
