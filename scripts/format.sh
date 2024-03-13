#!/bin/sh -e

python3 -m ruff check protopy --fix
python3 -m ruff format protopy
