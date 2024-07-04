#!/bin/sh

if test -f ".env"; then
  echo "Found an environment file"
  source "$FILE"
fi

python3 src/main.py "$@"