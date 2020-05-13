#!/bin/sh

docker-compose -f docker/docker-compose.yml build goonk9320 goonk9321 goonk9322 goonk9323
docker-compose -f docker/docker-compose.yml down
docker-compose -f docker/docker-compose.yml up -d
