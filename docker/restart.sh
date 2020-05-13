#!/bin/sh

docker-compose -f docker/docker-compose-dev.yml build goonk9320
docker-compose -f docker/docker-compose-dev.yml down
docker-compose -f docker/docker-compose-dev.yml up
