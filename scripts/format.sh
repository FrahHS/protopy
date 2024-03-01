#!/bin/sh -e

python3 -m ruff protopy --fix
python3 -m ruff format protopy
