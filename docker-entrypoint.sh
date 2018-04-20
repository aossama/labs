#!/usr/bin/env sh

set -e

cmd=${1}

if [ "${cmd}" == 'gunicorn' ]; then
    gunicorn app:app \
        --name labs \
        --bind 0.0.0.0:8000 \
        --workers 3 \
        --log-file - \
        --access-logfile - \
        --error-logfile -
fi

exec "$@"
