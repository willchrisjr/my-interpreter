#!/bin/sh

# Exit early if any commands fail
set -e

exec pipenv run python3 -m app.main "$@"