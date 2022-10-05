#!/bin/bash

required_env_keys='
    GCP_PROJECT_ID
    GCP_SERVICE_NAME
    GCP_REGION
    CLOUDSQL_INSTANCES
    DB_USER
    DB_PASS
    DB_NAME
    GCP_SERVICE_ACCOUNT
    ENV_VERSION'

#
# Get all keys in .env_cloud_run file and assert they are in the list of required keys
#

# Get all keys in .env_cloud_run file
env_keys=$(cat .env_cloud_run | cut -d '=' -f 1)

# Assert all required keys are in the .env_cloud_run file
for key in $required_env_keys; do
  if [[ ! $env_keys =~ $key ]]; then
    echo "Missing key $key in .env file"
    exit 1
  fi
done

# Get all env vars from .env_cloud_run file and export them. Filter comments and empty lines
export $(cat .env_cloud_run | grep -v '^#' | grep -v '^$' | xargs)

# Build
gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/$GCP_SERVICE_NAME

# Deploy
gcloud run deploy $GCP_SERVICE_NAME \
    --image gcr.io/$GCP_PROJECT_ID/$GCP_SERVICE_NAME \
    --platform managed \
    --region $GCP_REGION \
    --allow-unauthenticated \
    --project $GCP_PROJECT_ID \
    --add-cloudsql-instances=m-private-org:us-central1:m-private-mysql \
    --set-env-vars GCP_PROJECT_ID=$GCP_PROJECT_ID,GCP_SERVICE_NAME=$GCP_SERVICE_NAME,GCP_REGION=$GCP_REGION,CLOUDSQL_INSTANCES=$CLOUDSQL_INSTANCES,DB_USER=$DB_USER,DB_PASS=$DB_PASS,DB_NAME=$DB_NAME,GCP_SERVICE_ACCOUNT=$GCP_SERVICE_ACCOUNT,ENV_VERSION=$ENV_VERSION