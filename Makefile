gcp-show-project-id::
	gcloud config get-value project

gcp-set-project-id::
	gcloud config set project m-private-org

gcp-build::
	gcloud builds submit --tag gcr.io/m-private-org/sars-fastapi

gcp-deploy::
	gcloud run deploy sars-fastapi \
		--image gcr.io/m-private-org/sars-fastapi \
		--platform managed \
		--region us-central1 \
		--add-cloudsql-instances=m-private-org:us-central1:m-private-mysql \
		--update-env-vars env_version=v2,env_tmp=tmp

gcp-build-deploy::
	make gcp-build
	make gcp-deploy

# gpc-add-service::
# 	gcloud run services update sars-fastapi --add-cloudsql-instances=m-private-org:us-central1:m-private-mysql
            

gcp-set-up::
	gcloud config set project m-private-org

gcp-login::
	gcloud auth login

# If already logged in and I need to change account
gcp-set-account::
	gcloud config set account ACCOUNT

open-in-browser::
	google-chrome https://sars-fastapi-dgyhb4jsxa-uc.a.run.app

get-my-external-ip::
	curl ifconfig.me


shell-load::
	docker-compose run --rm --service-ports loader /bin/bash

gcp-mysql-connect::
	mysql -u root -p -h 34.133.205.132

run-app::
	docker-compose run --rm --service-ports app


# https://cloud.google.com/sdk/gcloud/reference/auth/configure-docker#REGISTRIES
# gcloud auth configure-docker
# gcloud auth configure-docker gcr.io