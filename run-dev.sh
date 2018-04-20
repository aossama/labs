#!/usr/bin/env bash

export ENV_SETTINGS=/srv/conf/dev.cfg

docker container run -d --rm -e ENV_SETTINGS=${ENV_SETTINGS} --publish 8001:8000 --name labs-iam aossama/labs-iam
docker container run -d --rm -e ENV_SETTINGS=${ENV_SETTINGS} --publish 8002:8000 --name labs-auth --link labs-iam aossama/labs-auth
docker container run -d --rm -e ENV_SETTINGS=${ENV_SETTINGS} --publish 8003:8000 --name labs-labs aossama/labs-labs

docker container run -d --rm --name labs-ui --publish 8000:80 --link labs-iam --link labs-auth --link labs-labs aossama/labs-ui