#!/usr/bin/env bash

for service in iam auth labs; do
  echo "Building aossama/labs-${service}:latest"
  docker image build --rm -t aossama/labs-${service}:latest --build-arg service=${service} .
done

echo "Building aossama/labs-ui:latest"
cd ui/
docker image build --rm -t aossama/labs-ui:latest .