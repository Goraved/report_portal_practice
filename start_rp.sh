#!/usr/bin/env bash

curl https://raw.githubusercontent.com/reportportal/reportportal/master/docker-compose.yml -o docker-compose.yml

docker-compose -p reportportal up

open http://localhost:8080