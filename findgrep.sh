#!/bin/bash

pattern=$1
directory=$2
if [ -z "$diretory" ]; then
	directory='.'
fi
# -n : print
# =H : print
find . "$directory" -type f | xargs grep -nH "$pattern"
