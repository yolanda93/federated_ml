#!/bin/sh

docker build -t $1 .
parentdir="$(dirname "$(pwd)")"
docker run -it --rm -v $parentdir/$1/notebooks:/workspace/notebooks $1 /sh/bin
