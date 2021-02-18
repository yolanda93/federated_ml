#!/bin/sh

folder=""  # Default to empty folder
parentdir="$(dirname "$(pwd)")"

# Parse options to the `launch` command
while getopts ":h" opt; do
  case ${opt} in
    h )
      echo "Usage:"
      echo "    launch -h                   Display this help message."
      echo "    launch create <folder>      Create docker image and mount <folder>."
      echo "    launch run <folder>         Run docker image and mount <folder>"
      exit 0
      ;;
   \? )
     echo "Invalid Option: -$OPTARG" 1>&2
     exit 1
     ;;
  esac
done

subcommand=$1; shift
folder=$1
case "$subcommand" in
  create)
    echo Creating $folder ...
    docker build -t $folder .
    docker run -it --rm -v $parentdir/$folder/notebooks:/workspace/notebooks $folder /sh/bin
  ;;
  run)
    echo Running $folder ...
    docker run -it --rm -v $parentdir/$folder/notebooks:/workspace/notebooks $folder /sh/bin 
esac
