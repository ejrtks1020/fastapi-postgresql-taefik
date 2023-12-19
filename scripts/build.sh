#!/bin/bash
DOCKER_BUILDKIT=1 docker build --target=runtime -t my-app -f ../Dockerfiles/Dockerfile ..
