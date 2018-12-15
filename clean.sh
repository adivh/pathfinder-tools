#!/bin/bash

no_change=True
count_pyc=`find ./src -maxdepth 1 -name "*.pyc" | wc -l`

if [ $count_pyc -gt 0 ]; then
    rm ./src/*.pyc
    echo $count .pyc-files removed
    no_change= False
fi

if [ -e ./src/__pycache__ ]; then
    rm -r ./src/__pycache__
    echo Removed __pycache__
    no_change= False
fi

if [ no_change ]; then
    echo no changes made: project is already clean
fi