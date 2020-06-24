#!/bin/bash

pattern=$1
directory=$2
name=$3
if [ -z "$diretory" ]; then
	directory='.'
fi
if [ -z "$name" ]; then
	name='*'
fi
# -n : print
# =H : print
find . "$directory" -type f | xargs grep -nH "$pattern"
