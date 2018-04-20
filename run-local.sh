#!/usr/bin/env bash

daemonize() {
    service=${1}
    port=${2}

    gunicorn ${service}.app:app \
        --env ENV_SETTINGS=conf/local.cfg \
        --pythonpath ./${service} \
        --name labs \
        --bind 0.0.0.0:${port} \
        --workers 1 \
        --log-level=debug \
        --log-file logs/${service}.log \
        --access-logfile logs/${service}.log \
        --pid /tmp/${service}.pid \
        --daemon
}

echo "Starting IAM service"
daemonize iam 8001

echo "Starting Labs service"
daemonize labs 8003

echo "Starting Auth service"
daemonize auth 8002
