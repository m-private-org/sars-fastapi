# FastAPI microservice with DataBase
This project is meant to create a basic example on how to create a micro-service with fast-api.

## Features
- Local DB
- GCP Cloud Run and GCP SQL integration

## SetUp and Run

### SetUp and Run Locally with Local DB
- `./run_load_local_db.sh`
- `./run_app_local_db.sh`

### Build and Deploy to Cloud Run
- TODO: Instruction to get and set up the right env values
- `./build_and_deploy_to_cloud_run.sh`

## TODO:
- Extract example model and endpoint to its own module
- Use pydantic settings: https://fastapi.tiangolo.com/advanced/settings/#pydantic-settings


# SARS-API
blog: https://towardsdatascience.com/fastapi-cloud-database-loading-with-python-1f531f1d438a


## Set up
- copy sample.env to .env

## Dev Instructions
Run `pipenv install --dev` to install the env.  
Run `pipenv run pre-commit install` to initialize the git hooks.  
Run `pipenv run pre-commit run --all-files` if there are file that were committed before adding the git hooks.  
Activate the shell with: `pipenv shell`  
Lint with: `pylint app` and `pylint load.py`

## Build and Run the App With Docker (Dev)
Run `docker-compose build` to build the containers.  
Run `docker-compose up` to start the app.  
Run `docker-compose up -d` to start the app in detached mode.  
Run `docker-compose down` to stop the app.