#!/bin/sh

set -e

if [ -z "$1" ]; then
    # No args
    exec tail -f /dev/null
else
    # source home/app_user/app/.venv/bin/activate
    . "${APP_ROOT}/.venv/bin/activate"
    python "${APP_ROOT}/${DJANGO_APP_NAME}/${DJANGO_APP_NAME}/settings/dirs.py"
    exec $@
fi
