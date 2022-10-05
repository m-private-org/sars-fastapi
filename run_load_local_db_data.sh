#!/bin/bash

docker-compose -f docker-compose.yml -f docker-compose.local_db.yml --profile load_local_data run --rm loader
