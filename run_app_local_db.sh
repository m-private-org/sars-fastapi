#!/bin/bash

docker-compose -f docker-compose.yml -f docker-compose.local_db.yml --profile run_app up
